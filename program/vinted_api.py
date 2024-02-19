from json import dump, loads
from os import listdir, path, rename
from random import choice
from re import DOTALL, search
from time import sleep
from tkinter import Tk, messagebox
from requests import get, post, delete, put
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from engine import File, create_accounting_folder
from graphes import Graph


class VintedAPI:
    """Class to interact with API of Vinted"""

    def __init__(self, vinted_token:str):
        # accessors to language translationss
        self.lang_file = File("ressources/lang/"+str(File("settings/param.json").get_dict()["lang"])+".json")
        # get the id using get_current_url
        self.domain = "https://www.vinted.fr/"
        self.api_url = f"{self.domain}api/v2/"
        self.id = 00000 # the id of the user
        self._vinted_fr_session = vinted_token
        self.set_headers()
        self.anon_id = self.get_info_user(self.id, "anon_id")        
    
    def set_headers(self):
        """Set the headers with the session cookies"""
        self.headers = {
            "Host": "www.vinted.fr",
            "Cookie": f"_vinted_fr_session={self._vinted_fr_session}",
            "Sec-Ch-Ua": "",
            "Accept-Language": "en",
            "Sec-Ch-Ua-Mobile": "?0",
            "X-Datadog-Origin": "rum",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
            "X-Datadog-Sampling-Priority": "1",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Sec-Ch-Ua-Platform": "",
            "Origin": "https://www.vinted.fr",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate",
        }
        url = f"{self.domain}inbox"
        self.response = post(url, headers=self.headers)

        if self.check_response():
            html_code = self.response.text            
            # Extract the JSON data within the <script> tag
            pattern = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
            match = search(pattern, html_code, DOTALL)
            # Parse the JSON data
            json_data = loads(match.group(1))
            # Parse the JSON data inside json_data
            new_json_data = loads(json_data["props"]["pageProps"]["initialState"])
            # --- Update the tokens --- #
            self.csrf_token = new_json_data["next-env"]["CSRF_TOKEN"]
            self.headers['X-Csrf-Token'] = self.csrf_token

    def get_info_user(self, id:str, attribute:str):
        """Returns the value of the attribute according to the id
        
        Args:
            - id: id of the profile
            - attribute: key of the dict of the user
        """
        self.response = get(f"{self.api_url}users/{id}", headers=self.headers)
        if self.check_response():
            return self.response.json()['user'][attribute]
        else:
            if self.inform_status_connection() is None:
                if self.check_response() == False:
                    messagebox.showerror("URL incorrect", "The URL of the vintie account you entered is incorrect.\nChange it and try again, if you have no clue wich one to choose check out the tips")
                
    def is_connected(self):
        """Returns True if the user is connected"""
        self.response = get(f"{self.api_url}users/{self.id}", headers=self.headers)
        return self.check_response()
    
    def token_expired(self):
        """Displays a message to inform the user that his token has expired"""
        messagebox.showwarning(
            self.lang_file.get_page_text("connections_page", "token_expired_title"),
            self.lang_file.get_page_text("connections_page", "token_expired_desc")
        )
    
    def inform_status_connection(self):
        if not self.is_connected():
            self.token_expired()
            return False
        
    def get_number_followers(self, id:str):
        """Returns the number of followers of the user using its id"""
        url = f'{self.api_url}users/{id}/followed_users?per_page=100&page=1'
        response = get(url, headers=self.headers)
        json_response = response.json()

        if json_response["pagination"]["total_entries"] == 0:
            # the user does not follow anybody
            return False
    
    def send_notifications(self):
        """Sends messages to the users that like an item"""
        url = f"{self.api_url}notifications?page=1&per_page=1000"
        self.response = get(url, headers=self.headers)
        
        if self.check_response():
            notifications_json = self.response.json()["notifications"]
            
            for notification in notifications_json:
                # Check if it's a like notification
                if "added your" in notification["body"]:
                    if self.check_date_notif(notification["updated_at"]):
                        parts = notification["body"].split("added")
                        url = search(rf'="\s*(.*?)\s*">', parts[1]).group(1).strip()
                        
                        # --- Check if the product is still available --- #
                        self.response = get(url, headers=self.headers)
                        
                        if self.check_response():
                            # --- Check if the notification has already been read --- #
                            if notification["is_read"] == False:
                                self.send_msg_notif(notification, parts)

    def check_date_notif(self, date_string:str):
        """Returns True if notification is between 12 hours and 1 week"""
        date_string = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
        now = datetime.now(date_string.tzinfo)
        time_difference = now - date_string
        
        # Check if the time difference is within the specified range
        if time_difference < timedelta(weeks=1):
            return True
        return False
    
    def send_msg(self, msg:str, conv_id:str):
        """Sends a message to a user
        
        Args:
            - {str} msg: message for the user
            - {str} conv_id: conversation's id
        """
        url = f"{self.api_url}conversations/{conv_id}/replies"
        data = {"reply":{"body": msg,"photo_temp_uuids": None}}
        post(url, headers=self.headers, json=data)

    def send_msg_notif(self, notification:dict, parts:list):
        """Send a notification message to a user
        
        Args:
            - {dict} notification: data related to the notification
            - {list} parts: notifications splited in 2 parts
        """
        pseudo = search(rf">\s*(.*?)\s*</a>", parts[0]).group(1).strip()
        id = search(rf'"\s*(.*?)\s*"', parts[0]).group(1).strip().split("/")[-1].split("-")[0]
        product = search(rf">\s*(.*?)\s*</a>", parts[1]).group(1).strip()
                                
        # --- Send a message to the user --- #
        msg = f"Bonjour {pseudo},\nSeriez-vous intéressé par : {product} ?\nSouhaitez-vous également créer une offre groupée de plusieurs articles ? Dans ce cas, envoyez-nous un message s'il vous plaît.\n\nLa Bro'tique"
        
        if self.get_info_user(id, "gender") == "F":
            msg.replace("intéressé", "intéressée")
        if datetime.now().hour >= 20:
            msg = msg.replace("Bonjour", "Bonsoir")
        self.response = get(self.domain[:-1]+notification["link"], headers=self.headers)
        
        try:
            conv_id = search(rf'rel="alternate" href="\s*(.*?)\s*" hrefLang="fr-FR"', self.response.text).group(1).strip().split("/")[-1]
            url = f"{self.api_url}conversations/{conv_id}/replies"
            data = {"reply":{"body": msg,"photo_temp_uuids": None}}
            post(url, headers=self.headers, json=data)
        except:
            pass       

    def get_nb_items(self):
        """Returns the number of available items"""
        url = f"{self.api_url}users/{self.id}/items?page=1&per_page=96&order=relevance"
        self.response = get(url, headers=self.headers)
        
        if self.check_response():
            nb_items = self.response.json()["pagination"]["total_entries"]
            return nb_items if nb_items !=0 else False
        else:
            return False
    
    def check_response(self) -> bool:
        """Returns True if the request has been executed"""
        return self.response.status_code == 200

    def del_sold_items(self):
        """Deletes the ads that can be deleted"""
        url = f"{self.api_url}users/{self.id}/items?page=1&per_page=96&order=revelance"
        self.response = get(url, headers=self.headers)
        json_data = self.response.json()
        items = json_data["items"]
        nb_pages = json_data["pagination"]["total_pages"]
        i = 1
        while i <= nb_pages:
            for j in range(len(items)):
                if items[j]["can_delete"] == True and items[j]["is_closed"] == 1:
                    item_id = items[j]["id"]
                    url = f"{self.api_url}items/{item_id}/delete"
                    post(url, headers=self.headers)
            i += 1
            url = f"{self.api_url}users/{self.id}/items?page={i}&per_page=96&order=revelance"
            self.response = get(url, headers=self.headers)
            json_data = self.response.json()
            items = json_data["items"]

    def delete_all_ads(self):
        """Deletes all ads of the profile"""        
        messagebox.showwarning("PAY ATTENTION", "You are about to delete all of your ads")
        if messagebox.askokcancel("Delete all ads", "Do you realy want to continue\nThis action can not be undone!") != True:
            return
        url = f"{self.api_url}users/{self.id}/items?page=1&per_page=96&order=revelance"
        self.response = get(url, headers=self.headers)
        json_data = self.response.json()
        items = json_data["items"]
        nb_pages = json_data["pagination"]["total_pages"]
        # number of ad deleted in the same row
        nb_ad_deleted = 0
        i = 1
        while i <= nb_pages:
            for j in range(len(items)):
                item_id = items[j]["id"]
                url_suppr = f"{self.api_url}items/{item_id}/delete"
                self.response = post(url_suppr, headers=self.headers)
                if not self.check_response():
                    return messagebox.showerror("Backup recovery failure", f"An error occured while deleting your ads \
                                                We have been able to delete {nb_ad_deleted} ads \
                                                \nPlease try again, it might be due to an overflow of requests. \
                                                Do not forget to refresh your token")
                nb_ad_deleted += 1
            i += 1
            self.response = get(url, headers=self.headers)
            json_data = self.response.json()
            items = json_data["items"]

    def clear_conversations(self, nb_month:int):
        """Manage conversations: deletes old conversations and leave feedbacks
        
        Arg:
            - {int} nb_month: minimum number of month
        """
        url = f"{self.api_url}inbox?page=1&per_page=100"
        self.response = get(url, headers=self.headers)
        if self.check_response():
            conversations = self.response.json()["conversations"]
            nb_conversations = self.response.json()["pagination"]["total_entries"]            
            if nb_conversations != 0:
                nb_page = nb_conversations//100+1 if nb_conversations%100 != 0 else nb_conversations//100
                # Goes through all the pages
                i = 1
                while i <= nb_page:
                    n = len(conversations)
                    # Goes through all the conversations of the page
                    for j in range(n):
                        conv_id = conversations[j]["id"]
                        url = f"{self.api_url}conversations/{conv_id}"
                        self.response = get(url, headers=self.headers)
                        if self.check_response():
                            try:
                                status = self.response.json()["conversation"]["transaction"]["status"]
                                
                                if status == 450:
                                    # --- Leave a feedback to the user --- #
                                    self.leave_feedback(conversations[j])
                            except:
                                pass                                
                        try:
                            # Check if the time difference is within the specified range
                            date_string = conversations[j]["updated_at"]
                            date_string = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
                            now = datetime.now(date_string.tzinfo)
                            time_difference = now - date_string
                            if time_difference >= timedelta(weeks=4*nb_month):
                                self.del_conv(conversations[j]["id"])
                            else:
                                pass
                        except:
                            pass

                    # --- Update the conversations data --- #
                    i += 1
                    url = f"{self.api_url}inbox?page={i}&per_page=100"
                    self.response = get(url, headers=self.headers)
                    if self.check_response():
                        conversations = self.response.json()["conversations"]

    def leave_feedback(self, conversation):
        """Leaves a feedback"""
        transaction_id = self.response.json()["conversation"]["transaction"]["id"]
        user_id = self.response.json()['conversation']['opposite_user']['id']
        url = f"{self.api_url}user_feedbacks"
        data = {
            "user_id": user_id,
            "feedback": choice(File("ressources/secretariat/msg.json").get_dict()["feedbacks"]),
            "rating": 5,
            "transaction_id": transaction_id
        }
        self.response = post(url, headers=self.headers, json=data)
        self.del_conv(conversation["id"])
        
    def del_conv(self, conv_id):
        """Deletes a conversation"""
        delete(f"{self.api_url}conversations/{conv_id}", headers=self.headers)

    def refresh_ads(self):
        """Refreshes ads available of the profile"""
        url = f"{self.api_url}users/{self.id}/items?page=1&per_page=96&order=revelance"
        self.response = get(url, headers=self.headers)
        json_data = self.response.json()
        items = json_data["items"]
        nb_pages = json_data["pagination"]["total_pages"]
        same_row = 0 # count the number of ad reuploaded in the same row
        i = 1
        while i <= nb_pages:
            for j in range(len(items)):
                iI = items[j] # itemInfo
                # if ad not available
                if iI["is_visible"] == 0:
                    return
                # --- Prepare the json data --- #
                # colors if required
                color_ids = []
                for color in [iI["color1_id"], iI["color2_id"]]:
                    if color != None:
                        color_ids.append(color)
                color_ids = None if len(color_ids)==0 else color_ids
                # list of urls containing photos
                url_photo = []
                for photo in items[j]["photos"]:
                    for thumbnails in photo["thumbnails"]:
                        if thumbnails["type"] == "thumb364x428":
                            url_photo.append(thumbnails["url"])
                infos_item = {
                    "id": None,
                    "currency": iI["price"]["currency_code"],
                    "title": iI["title"],
                    "description": iI["description"],
                    "brand_id": iI["brand_id"],
                    "brand": iI["brand"],
                    "size_id": iI["size_id"],
                    "catalog_id": iI["catalog_id"],
                    "isbn": iI["isbn"],
                    "is_unisex": iI["is_unisex"],
                    "is_for_sell": True,
                    "status_id": iI["status_id"],
                    "video_game_rating_id": iI["video_game_rating_id"],
                    "price": iI["price"]["amount"],
                    "package_size_id": iI["package_size_id"],
                    "shipment_prices": {
                        "domestic": None,
                        "international": None
                    },
                    "color_ids": color_ids,
                    "assigned_photos": [],
                    "measurement_length": iI["measurement_length"],
                    "measurement_width": iI["measurement_width"],
                    "item_attributes": iI["item_attributes"]
                }
                if same_row == 15:
                    # wait to avoid beeing blocked by the server
                    sleep(30)
                    same_row = 0
                if self.reupload_item(infos_item, url_photo):
                    # delete the ad
                    item_id = iI["id"]
                    url = f"{self.api_url}items/{item_id}/delete"
                    post(url, headers=self.headers)
                    same_row += 1
                else:
                    messagebox.showerror("Reupload failed", "We failed to reupload " + iI["title"] + "\nYou will have to post it on your own. We are sorry for this, it may be due to an overflow of requests and an automatic response of the servers of Vinted")
            # next ads json page       
            i += 1
            url = f"{self.api_url}users/{self.id}/items?page={i}&per_page=96&order=revelance"
            self.response = get(url, headers=self.headers)
            json_data = self.response.json()
            items = json_data["items"]

    def reupload_item(self, infos_item:dict, url_photo:list):
        """Reupload an item on Vinted to bump it
        
        Args:
            - {dict} infos_item: infos needed to upload an item        
            - {list} photos: list of urls with the photos of the ad
        """
        headers = {
            'Host': 'www.vinted.fr',
            'X-Csrf-Token': self.csrf_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Ch-Ua-Platform': '""',
            'Origin': 'https://www.vinted.fr',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate',            
            "Cookie": f"_vinted_fr_session={self._vinted_fr_session}",
            "Sec-Ch-Ua": "",
        }

        # --- Generate temp uuid --- #
        url = "https://www.vinted.fr/items/new"
        r = get(url, headers=headers)
        temp_uuid = search(rf'<div id="ItemUpload-react-component-\s*(.*?)\s*"', r.text).group(1).strip()
        
        # --- Upload photos --- #        
        list_id_photos = []

        for i, url in enumerate(url_photo):
            self.response = get(url)

            if self.check_response():
                file=[
                    ('photo[file]', (f'{i}.jpg', self.response.content, 'image/jpeg'))
                ]
            url = "https://www.vinted.fr/api/v2/photos"
            payload = {
                'photo[type]': 'item',
                'photo[temp_uuid]': temp_uuid
            }
            r = post(url, headers=headers, data=payload, files=file)
            list_id_photos.append(r.json()["id"])

        # --- Update the infos_item --- #
        infos_item["temp_uuid"] = temp_uuid
        for id in list_id_photos:
            photo = {
                "id": id,
                "orientation": 0
            }
            infos_item["assigned_photos"].append(photo)
        json_item = {
            "item": infos_item,
            "feedback_id": None
        }

        # --- Upload the item --- #
        url = "https://www.vinted.fr/api/v2/items"
        self.response = post(url, headers=headers, json=json_item)

        if self.check_response():
            return True
        return False 

    def photo_shoot_prep_ad(self, brand_name:str):
        """Needed for photo shoot. In developpement"""
        brand_url = f"https://www.vinted.fr/api/v2/brands?keyword={brand_name}"
        brand_list = self.response.json()["brands"]
        if len(brand_list) == 0:
            print("You did not enter a known brand, please make sure to use the exact name of the brand available on Vinted")
            # re ask for the brand
        for brand in self.response.json()["brands"]:
            print(brand)
        statuses = {
            "New with tags": 6,
            "New without tags":1,
            "Very good":2,
            "Good":3,
            "Satisfactory":4
        }
        package_sizes = {
            "Small":1,
            "Medium":2,
            "Large":3
        }
        video_game_ratings = {
            "AO - Adults only":175,
            "E – Everyone":170,
            "E10+ – Everyone 10+":171,
            "M - Mature 17+":173,
            "PEGI 12":162,
            "PEGI 16":164,
            "PEGI 18":163,
            "PEGI 3":160,
            "PEGI 7":161,
            "RP - Rating pending":174,
            "T – Teen 13+":172,
            "USK 0":165,
            "USK 12":167,
            "USK 16":168,
            "USK 18":169,
            "USK 6":166,
            "Unspecified":176
        }

    def get_shipping_label(self, thread:str):
        """Gets shipping label
        
        Arg:
            - {str} thread: link of the transaction
        """
        # --- Initialization --- #       
        # get the id from the link in the email
        conv_id = search(rf'id=\s*(.*?)\s*&l=', thread).group(1).strip()
        url = f"{self.api_url}conversations/{conv_id}"
        self.response = get(url, headers=self.headers)
        if self.check_response():
            conversation_data = self.response.json()["conversation"]
            transaction_id = conversation_data["transaction"]["id"]
            pseudo = conversation_data["opposite_user"]["login"]
        
        # --- Generates shipping label --- #
        # get shipping label > click
        click_data = [{"event":"user.click","anon_id":self.anon_id,"user_id":self.id,"lang_code":"en-fr","extra":{"screen":"message_list","path":f"/inbox/{conv_id}","target":"get_shipping_label","target_details":"{\"transaction_id\":"+str(transaction_id)+"}"},"time":1688741243877}]
        # get shipping label > view details
        details_data = [{"event":"seller.view_add_contact_details","anon_id":self.anon_id,"user_id":self.id,"lang_code":"en-fr","extra":{"screen":"get_shipping_label","path":f"/inbox/{conv_id}","transaction_id":transaction_id},"time":1688741243903}]
        # get shipping label > confirm
        confirm_data = [{"event":"user.click","anon_id":self.anon_id,"user_id":self.id,"lang_code":"en-fr","extra":{"screen":"get_shipping_label","path":f"/inbox/{conv_id}","target":"confirm","target_details":"{\"transaction_id\":"+str(transaction_id)+"}"},"time":1688741266860}]
        url = f"{self.domain}relay/events"
        for data in [click_data, details_data, confirm_data]:
            post(url, headers=self.headers, json=data)        
        # get shipping label > finalize
        url = f"{self.api_url}transactions/{transaction_id}/shipment/order"
        seller_address_id = self.get_info_user(self.id, "default_address")["id"]
        data = {"seller_address_id":seller_address_id}
        self.response = put(url, headers=self.headers, json=data)

        # --- Message of thanks --- #
        if self.check_response():            
            msg = File("ressources/secretariat/msg.json").get_dict()["sold"]                        
            if datetime.now().hour >= 20:
                msg = msg.replace("Bonjour", "Bonsoir")
            msg = msg.replace("pseudo", pseudo)
            self.send_msg(msg, conv_id)

    def upload_item(self, infos_item:dict, photos_path:str, prevent_user=True):
        """Uploads an item on Vinted according to its template
        
        Args:
            - {dict} infos_item: infos needed to upload an item
            - {str} photos_path: path to the folder with photos
            - {bool} prevent_user: True if messagebox needed
        """
        headers = {
            'Host': 'www.vinted.fr',
            'X-Csrf-Token': self.csrf_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Ch-Ua-Platform': '""',
            'Origin': 'https://www.vinted.fr',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate',            
            "Cookie": f"_vinted_fr_session={self._vinted_fr_session}",
            "Sec-Ch-Ua": "",
        }
        # --- Generate temp uuid --- #
        url = "https://www.vinted.fr/items/new"
        r = get(url, headers=headers)
        temp_uuid = search(rf'<div id="ItemUpload-react-component-\s*(.*?)\s*"', r.text).group(1).strip()
        
        # --- Upload photos --- #
        url = "https://www.vinted.fr/api/v2/photos"
        payload = {
            'photo[type]': 'item',
            'photo[temp_uuid]': temp_uuid
        }
        list_id_photos = []

        for i in range(1, len(listdir(photos_path))+1):
            file_path = photos_path+f'{i}.jpg'
            file=[
                ('photo[file]',(f'{i}.jpg', open(file_path,'rb'), 'image/jpeg'))
            ]
            self.response = post(url, headers=headers, data=payload, files=file)
            if not self.check_response():
                if prevent_user:
                    return messagebox.showerror("Upload failure", "We failed to upload " + infos_item["title"] + "\nYou will have to post it on your own. We are sorry for this, it may be due to an overflow of requests and an automatic response of the servers of Vinted")
            list_id_photos.append(self.response.json()["id"])
        
        # --- Update the infos_item --- #
        infos_item["temp_uuid"] = temp_uuid
        for id in list_id_photos:
            photo = {
                "id": id,
                "orientation": 0
            }
            infos_item["assigned_photos"].append(photo)            
        json_item = {
            "item": infos_item,
            "feedback_id": None
        }

        # --- Upload the item --- #
        url = "https://www.vinted.fr/api/v2/items"
        self.response = post(url, headers=headers, json=json_item)

        if self.check_response():
            if prevent_user:
                messagebox.showinfo("Ad posted succesfully", infos_item["title"] + " has been uploaded succesfully!")
        else:
            messagebox.showerror("Upload failure", "We failed to upload " + infos_item["title"] + "\nYou will have to post it on your own. We are sorry for this, it may be due to an overflow of requests and an automatic response of the servers of Vinted")

    def recover_followed_users(self):
        """Recovers the backup of vinties the user subscribed to"""
        self.short_pause = 31
        self.long_pause = 101
        f_path = "ressources/backup_followed_users.json"
        if not path.exists(f_path):
            return messagebox.showinfo("No backup found", "You do not have a backup")
        
        # --- Get the user's followed users --- #
        url_fu = f"{self.api_url}users/{self.id}/followed_users?per_page=90&page=1!"
        json_data = get(url_fu, headers=self.headers).json()
        pagination = json_data["pagination"]
        users = json_data["users"]
        nb_pages = pagination["total_pages"]
        
        i = 1
        while i <= nb_pages:            
            users = get(url_fu, headers=self.headers).json()["users"]
            for user in users:
                if self.long_pause == 100:
                    sleep(60)
                    self.long_pause = 0
                if self.short_pause == 30:
                    sleep(10)
                    self.short_pause = 0
                # --- Unfollow user --- #
                data = {"type":"user","user_favourites":[user["id"]]}
                url = f"{self.api_url}user_favourites/toggle"
                self.response = post(url, headers=self.headers, json=data)
                if not self.check_response():
                    return messagebox.showerror("Unfollowing process failure", "An error occured while unfollowing vinties.\nPlease try again, it might be due to an overflow of requests")
                self.short_pause += 1
                self.long_pause += 1
            i += 1
        
        # --- Recover following --- #
        for user_id in loads(open(f_path).read())["users"]:
            # --- Follow user --- #
            data = {"type":"user","user_favourites":[user_id]}
            url = f"{self.api_url}user_favourites/toggle"
            self.response = post(url, headers=self.headers, json=data)
            if not self.check_response():
                return messagebox.showerror("Backup recovery failure", "An error occured while recovering your backup.\nPlease try again, it might be due to an overflow of requests")
        messagebox.showinfo("Backup successfully recovered", "You have recovered all your previous vinties that you were following")

    def get_followers(self, id_user:int):
        """Returns 0 if the user has no followers else it returns the list of ids of followers"""
        url_f = f"{self.api_url}users/{id_user}/followers?per_page=90&page=1"
        self.response = get(url_f, headers=self.headers)
        pagination = self.response.json()["pagination"]
        nb_followers = pagination["total_entries"]
        if nb_followers == 0:
            return 0
        list_followers = []
        nb_pages = pagination["total_pages"]
        users = self.response.json()["users"]
        i = 1
        while i <= nb_pages:
            users = get(url_f, headers=self.headers).json()["users"]
            for user in users:
                if user["is_favourite"] == False and user["id"] != self.id:
                    list_followers.append(user["id"])
            i += 1
        return list_followers
    
    def get_followed_users(self, id_user:int):
        """Returns 0 if the user has no followed users else it returns the list of ids of followed users"""
        url_fu = f"{self.api_url}users/{id_user}/followed_users?per_page=90&page=1!"
        self.response = get(url_fu, headers=self.headers)
        pagination = self.response.json()["pagination"]
        nb_followed_users = pagination["total_entries"]
        if nb_followed_users == 0:
            return 0
        list_followed_users = []
        nb_pages = pagination["total_pages"]
        users = self.response.json()["users"]
        i = 1
        while i <= nb_pages:
            users = get(url_fu, headers=self.headers).json()["users"]
            for user in users:
                if user["is_favourite"] == False and user["id"] != self.id:
                    list_followed_users.append(user["id"])
            i += 1                
        return list_followed_users
    
    def backup_followed_users(self):
        """Saves the vinties that the user is following before starting a follow mass wave"""
        # --- Get the user's followed users --- #
        url_fu = f"{self.api_url}users/{self.id}/followed_users?per_page=90&page=1!"
        self.response = get(url_fu, headers=self.headers)
        pagination = self.response.json()["pagination"]
        nb_followed_users = pagination["total_entries"]

        # --- Back up the followed people of the user --- #
        if nb_followed_users != 0:
            self.list_followed_users = {"users": []}
            users = self.response.json()["users"]
            nb_pages = pagination["total_pages"]
            i = 1
            while i <= nb_pages:
                users = get(url_fu, headers=self.headers).json()["users"]
                for user in users:
                    self.list_followed_users["users"].append(user["id"])
                i += 1
            
            if self.erase_backup == True:
                # save the backup
                with open("ressources/backup_followed_users.json", "w", encoding="utf-8") as f:
                    dump(self.list_followed_users, f, indent=4, ensure_ascii=False)

    def follow_mass_my_reviews(self):
        """Follows all the vinties which whom the user had a transaction"""
        self.erase_backup = messagebox.askyesnocancel("Erase backup", "You are about to follow the vinties which whom you had a transaction. Do you want to erase your backup of followed users? Press No if you want to keep the previous backup")
        if self.erase_backup == None:
            return

        # backup followed users
        self.backup_followed_users()

        i = 1
        url_feedbacks = f"{self.api_url}user_feedbacks?user_id={self.id}&page={i}&per_page=100&by=all"
        self.response = get(url_feedbacks, headers=self.headers)
        pagination = self.response.json()["pagination"]
        
        if pagination["total_entries"] == 0:
            messagebox.showinfo("No feedback", "You do not have any feedack. So there is no person to follow. Come back later and keep going for your buisness!")
            return
        
        # --- Loop to follow everyone --- #
        nb_pages = pagination["total_pages"]
        feedbacks_list = self.response.json()["user_feedbacks"]
        url_follow = f"{self.api_url}user_favourites/toggle"
        nb_vintie_followed = 0
        self.short_pause = 31
        self.long_pause = 101

        while i <= nb_pages:
            for feedback in feedbacks_list:
                if feedback["user"]["is_favourite"] == False:
                    # follow user
                    if self.short_pause == 30:
                        sleep(10)
                        self.short_pause = 0
                    if self.long_pause == 100:
                        sleep(60)
                        self.long_pause = 0
                    data = {"type":"user","user_favourites":[feedback["user"]["id"]]}
                    self.response = post(url_follow, headers=self.headers, json=data)
                    if not self.check_response():
                        messagebox.showinfo("Follow wave not completed", f"You have successfully followed {nb_vintie_followed}")
                        return
                    nb_vintie_followed += 1
                    # increase timers
                    self.short_pause += 1
                    self.long_pause += 1
            
            i += 1
            url_feedbacks = f"{self.api_url}user_feedbacks?user_id={self.id}&page={i}&per_page=100&by=all"
            self.response = get(url_feedbacks, headers=self.headers)
            feedbacks_list = self.response.json()["user_feedbacks"]
        # inform the user that the function is completed
        messagebox.showinfo("Follow mass completed", f"We have been able to follow {nb_vintie_followed} succesfully!")
        
    def follow_mass(self, nb_to_flw:int):
        """Backup the previous list of followed users and follow a certain number of users

        Arg:
            - {int} nb_to_flw: number of users to follow
        """
        if nb_to_flw == 1:
            desc = f"You are about to follow {nb_to_flw} vintie.\n\nDo you want to update your backup?\nIt will erase your previous backup if you accept"
        else:
            desc = f"You are about to follow {nb_to_flw} vinties.\n\nDo you want to update your backup?\nIt will erase your previous backup if you accept"
        
        self.erase_backup = messagebox.askyesnocancel("Erase backup", desc)
        if self.erase_backup == None:
            return
        
        # --- Get the user's followers --- #
        url = f"{self.api_url}users/{self.id}/followers?per_page=90&page=1"
        self.response = get(url, headers=self.headers)
        pagination = self.response.json()["pagination"]
        nb_followers = pagination["total_entries"]
        # --- Get the user's followed users --- #
        url_fu = f"{self.api_url}users/{self.id}/followed_users?per_page=90&page=1!"
        self.response = get(url_fu, headers=self.headers)
        pagination = self.response.json()["pagination"]
        nb_followed_users = pagination["total_entries"]

        # case where we can not start the function
        if nb_followed_users == 0 and nb_followers == 0:
            messagebox.showinfo("You do not follow anyone", "You should follow at least one person before using this feature, preferably someone who has multiple followers and also follows other users. We recommend using the functionality to follow all the followers of a Vinted user. You can also choose to follow the users that someone follows on Vinted")
            return
        
        # --- Prepare recursive program --- #
        self.nb_user_followed = 0
        self.short_pause = 0
        self.long_pause = 0
        IDS = [] # list that contains the ids to run the recursive program

        # --- Back up the followed people of the user --- #        
        if nb_followed_users != 0:
            self.backup_followed_users()            
            IDS += self.list_followed_users["users"]
        # use followers instead of followed users
        else:
            url_f = f"{self.api_url}users/{self.id}/followers?per_page=90&page=1"
            self.response = get(url_f, headers=self.headers)
            pagination = self.response.json()["pagination"]
            users = self.response.json()["users"]
            nb_pages = pagination["total_pages"]
            i = 1
            while i <= nb_pages:
                users = get(url_f, headers=self.headers).json()["users"]
                for user in users:
                    IDS.append(user["id"])
                i += 1
        
        def follow(users:list):
            """Goes through a list of ids and follow them"""
            for follower_id in users:
                if self.nb_user_followed < nb_to_flw:
                    if self.long_pause == 10:
                        sleep(5)
                        self.long_pause = 0
                    if self.short_pause == 1:
                        sleep(3)
                        self.short_pause = 0
                    # --- Follow user --- #
                    data = {"type":"user","user_favourites":[follower_id]}
                    url = f"{self.api_url}user_favourites/toggle"
                    self.response = post(url, headers=self.headers, json=data)
                    if self.check_response():
                        self.nb_user_followed += 1
                        self.short_pause += 1
                        self.long_pause += 1
                    else:
                        return False
                    IDS.append(follower_id)
                else:
                    return True

        def fm(id_user:int):
            """Recursive function that follows followed users and followers of id_user
            
            Arg:
                - {int} id_user: id of the user that we want to get social links from
            """
            # check followed users
            users = self.get_followed_users(id_user)
            if users == 0:
                # check followers
                users = self.get_followers(id_user)
                if users == 0:
                    return
                else:
                    result_follow = follow(users)
                    if result_follow == True:
                        return True
                    elif result_follow == False:
                        return False
            else:
                # follow all the followed users of the user
                result_follow = follow(users)
                if result_follow == True:
                    return True
                elif result_follow == False:
                    return False
                # follow all the followers of the user
                users = self.get_followers(id_user)
                if users == 0:
                    return
                else:
                    result_follow = follow(users)
                    if result_follow == True:
                        return True
                    elif result_follow == False:
                        return False
            
        # --- Going through the IDS --- #
        while len(IDS) > 0:
            # run the script for the first user
            fm_result = fm(IDS[0])
            if fm_result == True:
                return messagebox.showinfo("Follow wave completed", f"You have successfully followed {self.nb_user_followed} users")
            elif fm_result == False:
                return messagebox.showerror("Follow wave not completed", f"You have successfully followed {self.nb_user_followed} users out of {nb_to_flw} asked\n\nReason of failure: session has expired\nYou should relaunch the application and resume from where it stopped. Additionally, it is recommended not to exceed following a thousand vinties consecutively")
            # remove it from the list
            IDS.pop(0)
        return messagebox.showinfo("Follow wave not completed", f"You have successfully followed {self.nb_user_followed} users out of {nb_to_flw} asked")

    def follow(self, users:list):
        """Follows every vintie of a list of users"""
        self.long_pause = 101
        self.short_pause = 0
        vinties_scraped = 0
        for follower_id in users:                
            if self.long_pause == 100:
                sleep(60)
                self.long_pause = 0
            if self.short_pause == 30:
                sleep(3)
                self.short_pause = 0
            # --- Follow user --- #
            data = {"type":"user","user_favourites":[follower_id]}
            url = f"{self.api_url}user_favourites/toggle"
            self.response = post(url, headers=self.headers, json=data)
            if self.check_response():
                self.short_pause += 1
                self.long_pause += 1
                vinties_scraped += 1
            else:
                messagebox.showerror("Follow wave not completed", f"We have been able to scrap {vinties_scraped} from the profile.\nYou have been detected by the servers of Vinted.\nPlease refresh your token")
                return
        messagebox.showinfo("Follow wave completed", f"We have been able to scrap {vinties_scraped} from the profile")

    def get_id(self, url:str):
        """Returns the id contained in the url"""
        id = url.split("/")[-1].split("-")[0]
        # checks if the id is valid
        self.response = get(f"{self.api_url}users/{id}", headers=self.headers)
        if self.check_response() == False:
            messagebox.showerror("URL incorrect", "The URL of the vintie account you entered is incorrect.\nChange it and try again, if you have no clue wich one to choose check out the tips")
            return
        return id
    
    def scrap_followers_from(self, url_seller:str):
        """Follows every follower of a vinted seller"""
        id = self.get_id(url_seller)
        if id:
            users = self.get_followers(id)
            self.follow(users)

    def scrap_following_from(self, url_seller:str):
        """Follows every vintie that the seller is following"""
        id = self.get_id(url_seller)
        if id:
            users = self.get_followed_users(id)
            self.follow(users)    
    
    def export_month_notif(self, year:str, month:str):
        """Export the given month and prevent the user"""
        if self.export_month(year, month) == False:
            messagebox.showinfo("Month export", f"{month}/{year} has already been exported")
            return
        messagebox.showinfo("Month export", f"{month}/{year} has been exported successfully!")

    def export_month(self, year:str, month:str):
        """Export the given month"""
        url = f"{self.api_url}wallet/invoices/{year}/{month}"
        self.response = get(url, headers=self.headers)
        if not self.check_response():
            self.token_expired()
            return
        transactions = self.response.json()["invoice_lines"]
        accounting = self.lang_file.get_page_text("business_stats_page", "accounting")
        months = self.lang_file.get_page_text("business_stats_page", "months")

        # DO NOT CONTINUE IF THE MONTH HAS ALREADY BEEN EXPORTED
        if create_accounting_folder(f"{year}/{months}", month):
            return False
                
        # accessor to the months translation
        month_file = File(f"{accounting}/{year}/{months}/temp-{month}.xlsx")

        # ADD ALL VINTED TRANSACTIONS inside the temporary file
        for transaction in transactions:
            amount = float(transaction["amount"])
            title = transaction["title"]
            if not (title == "Withdrawal to bank account") and not (title == "Transfert vers le compte bancaire"):
                refund = True if title == "Refund" else False
                subtitle = transaction["subtitle"] # name of the product
                date = datetime.strptime(transaction["date"], "%Y-%m-%dT%H:%M:%S%z")
                date.strftime("%d/%m/%Y")
                date = date.date()
                line = {
                    "Date": date,
                    "Transaction": amount,
                    "Article": subtitle,
                    "Refund": refund
                }
                month_file.insertLine(line, ["Date", "Transaction", "Article", "Refund"])
        month_file.sort_by_date()
        # once exported the file is renamed without "temp"
        rename(f"{accounting}/{year}/{months}/temp-{month}.xlsx", f"{accounting}/{year}/{months}/{month}.xlsx")
    
    def get_previous_month(self) -> tuple:
        """Returns a tuple containing the year and the month of the previoius month"""
        previous_month = datetime.now() - relativedelta(months=1)
        return previous_month.year, previous_month.month

    def get_previous_trimester(self):
        """Returns a tuple containing the year and the number of the previous trimester"""
        # [[months of a trimester], number of the trimester]
        trimesters = [
            [[1, 2, 3], 4],
            [[4, 5, 6], 1],
            [[7, 8, 9], 2],
            [[10, 11, 12], 3]
        ]        
        today = datetime.now()
        
        for i in range(4):
            for j in range(3):
                if trimesters[i][0][j] == today.month:
                    if trimesters[i][1] == 4:
                        return today.year - 1, trimesters[i][1]
                    return today.year, trimesters[i][1]
    
    def get_first_month_trimester(self, num_trim:int) -> int:
        """Returns the first month of the trimester according to its number"""
        # (number of the trimester, first month of the previous trimester)
        trimesters = (
            (1, 1),
            (2, 4),
            (3, 7),
            (4, 10)
        )
        
        for i in range(4):
            if trimesters[i][0] == num_trim:
                return trimesters[i][1]
    
    def get_first_trimester(self, month:int) -> int:
        """Returs the number of the trimester of the starting trimester of the seller"""        
        # [[months of a trimester], first month of the trimester, number of the trimester]
        trimesters = [
            [[1, 2, 3], 1],
            [[4, 5, 6], 2],
            [[7, 8, 9], 3],
            [[10, 11, 12], 4]
        ]
        
        for i in range(4):
            for j in range(3):
                if trimesters[i][0][j] == month:
                    return trimesters[i][1]    

    def export_previous_trimester(self):
        """Exports the previous trimester"""
        year, trim_number = self.get_previous_trimester()
        # case where trimester not exported yet
        if self.export_trimester(year, trim_number, notif=True) == None:
            messagebox.showinfo("Trimester exportation", f"The trimester {trim_number} of {year} has been exported succesfully!")

    def export_trimester(self, year:int, trim_number:str, notif=False):
        """Creates a files with the Vinted transactions of the previous trimester
        
        Args:
            - {int} year: year of the trimester
            - {str} trim_number: number of the trimester
        """
        trimesters = self.lang_file.get_page_text("business_stats_page", "trimesters")
        accounting = self.lang_file.get_page_text("business_stats_page", "accounting")
        months_name = self.lang_file.get_page_text("business_stats_page", "months")

        # DO NOT CONTINUE IF THE TIMESTER HAS ALREADY BEEN EXPORTED
        if create_accounting_folder(f"{year}/{trimesters}", f"trim-{trim_number}"):
            if notif:
                messagebox.showinfo("Trimester export", f"The trimester {trim_number} from year {year} has already been exported. You can not redo this action unless if you delete the accounting file associated. Please make sure to backup your accounting files to avoid the risk of destroying everything and stay in the legality with your buissnes.\nEdit and move files ONLY IF YOU KNOW WHAT YOU ARE DOING!")
            return False

        # transactions from the previous trimester
        months = {
            "1": [1, 2, 3],
            "2": [4, 5, 6],
            "3": [7, 8, 9],
            "4": [10, 11, 12]
        }
        month = months[trim_number][0]
        # trimester file
        trim_file = File(f"{accounting}/{year}/{trimesters}/trim-{trim_number}.xlsx")

        for i in range(3):
            self.export_month(year, month+i)
            # copy the transactions from the months of the trimester
            month_file = File(f"{accounting}/{year}/{months_name}/{month+i}.xlsx")
            month_transactions = month_file.read_data()
            line = {
                    "Date": month_transactions["Date"],
                    "Transaction": month_transactions["Transaction"],
                    "Article": month_transactions["Article"],
                    "Refund": month_transactions["Refund"]
                }
            trim_file.insertLine(line, ["Date", "Transaction", "Article", "Refund"])
        trim_file.sort_by_date()
    
    def export_months(self, date:str, show_graph:bool=True):
        """Exports all the months since your first one
        
        Args:
            - {str} date: first trimester when the user started Vinted
            - {bool} show_graph: if True if displays statistical informations
        """
        # extract the year and the month of the 1st trimester
        year, month = date[:-3].split("-")
        year, month = int(year), int(month)

        # save the first month
        first_year = year
        first_month = month
        self.export_month(year, month)

        # --- Export months --- #
        prev_year, prev_month = self.get_previous_month()
        self.export_month(prev_year, prev_month)
        # labels and x axis for the graph
        months_labels = [self.lang_file.get_page_text("business_stats_page", "months_dict")[str(month)]]
        months_dates = [datetime(first_year, first_month, 1)]
        
        while not (year == prev_year and month == prev_month):            
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1
            months_labels.append(self.lang_file.get_page_text("business_stats_page", "months_dict")[str(month)])
            months_dates.append(datetime(year, month, 1))
            self.export_month(year, month)

        # --- Create the graph and the stats --- #
        if not show_graph:
            return
        # display the months graph
        Graph(months=True).plot_graph("months", first_year, prev_year, months_dates, months_labels)

    def export_trimesters(self, date:str, show_graph:bool=True):
        """Exports all the trimesters since your first one
        
        Args:
            - {str} date: first trimester when the user started Vinted
            - {bool} show_graph: if True if displays statistical informations
        """
        # extract the year and the month of the 1st trimester
        year, month = date[:-3].split("-")
        year, month = int(year), int(month)

        # get the first trimester
        trim_number = self.get_first_trimester(month)
        # save the first trimester values for the graph
        first_year = year
        # export the first trimester
        self.export_trimester(year, str(trim_number))

        # --- Export trimesters --- #
        # get the previous trimester
        prev_year, prev_trim_number = self.get_previous_trimester()
        self.export_trimester(prev_year, str(prev_trim_number))
        # labels and x axis for the graph
        trimester_labels = [f"Trim {trim_number}"]
        trimester_dates = [datetime(first_year, self.get_first_month_trimester(trim_number), 1)]

        while not (year == prev_year and trim_number == prev_trim_number):            
            if trim_number == 4:
                year += 1
                trim_number = 1
            else:
                trim_number += 1
            trimester_labels.append(f"Trim {trim_number}")
            trimester_dates.append(datetime(year, self.get_first_month_trimester(trim_number), 1))
            self.export_trimester(year, str(trim_number))

        # --- Create the graph and the stats --- #
        if not show_graph:
            return
        # display the trimesters graph
        Graph().plot_graph("trimesters", first_year, prev_year, trimester_dates, trimester_labels)

    def quick_get_brand_first_item(self):
        url = f"{self.api_url}users/{self.id}/items?page=1&per_page=96&order=revelance"
        self.response = get(url, headers=self.headers)
        print(self.response.json()["items"][0]["brand_id"])

# TO TEST: just replace with the access token
#vinted_api = VintedAPI("QXN4YjBkZVlRZTdYMHJZd1p3cWtsa1FSN3dsSVp1L2tMYmczUVEzaEFMK2xIUGRSbjMzdnFTUm5UUTJUK3ozTGRDbzc2bUhUakpKeitOajc5UGpRa1hIa01rMm5wNmpOQmllbWZCb0pYZXBzZ0QwQlU4eFVRSzliK2MyWmpDVTJOOTJpWXJtVjZWRnAxZXhvMm40clpDVG5PNDR4N3Jyb0k4b3BCWXI0anpONkhsYUlhaitXSWQyMHJpRmYxeStySVhTaUxuOEFNYmYrYVRFQmJOeE4zeGZOZFdzUkxGWm02QUlpaGtWUmNHKzQ4ZXFCT2NTZjFBSlRHQnc5Ulh0RU9rQ1VwVmExNUdOMHdtQlVxU3IyQlB1MTJwT0RaNGdva25wbk9XMlowTFRQQ3NDUHhmNlYxNFRFSkZqQmlWOGlwekswZ09qOWI3VjIxRVVHdWxiZ2JTMjRKTWJMQ0lGWm5HMklQL2hTRVoycUZKcWxOSmczZ2s1NmxtS3crT2xVVWR2d2JyQ01Xek83QjRpWG5HT29RMnhuNkU3MFFnam56KzkzRXJPMXJmZXcxZktZUm8rbmFsUFVyN25UVUNnZ1kxMjZjbU42K0NDWWVFWVJDQ2tCNXhHOXNxcnFOTWZ0Si85azh3Y3piT0EwMWY0VTlyT3VJUGx4S3JTR25yRTZpTGpUTWRYVHQxVVZ6OXpQSVArdW1TV0ZJN2NPOGR5WXZ6NEV0WjFkOGhaMVUwZGhXQXo4djRRYkxnNEVRT3ExRHJ5YXVBYlpEbEpNNDJxZ2ZLbVR5WllUQ1hyMWpBK1FqbE9GWGFhU3FnV2w1ZWRVem01NjhQTmZaOUxNUmxSSGxlRDljTGMzK01MTDgyY1E5S2svQ1dXc2w0VjV2VDZLQ0ZlVVFranZ5UTd6UU1qTmNWZk9FZzZFR2oyWlBIQ3RPbzNqSjNUNHM0d0xPOWh2MnpZWGl3bUgvY1NHdHhvckxFKzBLdUM3MXRsVUlXN3JNSUVBMG9BRU81Rk9VQmZyM3lkd3plbUtLK1RlRU5ORUpWOGZtaDNvS3V5STgyRDRLSUsxR3R0Q212aDZXNkZhUW8wQkp2WWx3VGFVNGZzVmdiWU90UEEvTlh3QmZyUStXWFpSc0xxU1ZBdTdCL3hKWkU1ZUNBeVhxYjlZeE5LNjlFREJVY3VWRWk3eUErMm5uOU5jTFoxQ3RpS25KZEh2MHVnUjAvSUw5UnlGQ1diUVBRUmx2Q2dlbHgybDFTeGxheS90UHpGVk8yS29vS0JsQkV5bTRITHZQU05hZUREOFRPUkIyL2I3MHNiOG5sYXczV2c1bDV2cDNYQTFUcmowTGowMzBreVJ3QlVDdEFrQXY2Uk9xcHhUeXZRdlFXZDFzZDlrK1drb3p6U05Edm1xMm1UTSt1UDZ5WEVTN2hSS09DQ0t0RTIvemorekFURXZzdWdXVUc4WGs1TEtzVSs4dGNna1d0UTZGZkFnN3h2YUpvbHlsc1NZTUZJTEljSmNkcW9DNEh4bS9ISUtkZU9hZkltZEhkUnMybUx5RjFDdWtIN3c3ZlcxS0piY1phVXVOQ0VpUmZubTl5dzNMWXlwaW9wQXdaRWxxeTdyNzNLb1dISlVnL3NkQTVUZWl3TlpVS3RJelpiQlpueElDMTFORUpPazRYY1BrampFaENpU2dSVFJoc011Z1NEdmtlNWt3aFlLdVo0R2Jxb3Yzbk1vZVhtR1dRPT0tLVVUQW1QZkUwZm5Zc2FmRWF1cG1HL1E9PQ%3D%3D--05309898aef046e6aa0a95584131b45729f2c4b5")


# TODO
# in the params change the id of the vinted fr session

# TODO
# get brand id auto for photo shoot and creation of templates/database/basic upload

# prevent the user to NEVER change the name of the accounting folders on a presentation
# of the app just copy or look or add data

# TODO
# refresh the oldest ads first (feature)
# refresh the lines indicated by the user


# TODO: in the database menu editor
# - add a tag from a known article
# - remove a tag from a known article
# - rename the article => update the tags.json


# TODO:
# backup ads avoid banishment / suppression