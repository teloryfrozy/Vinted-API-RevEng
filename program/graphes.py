# TODO
# --- advices ---
# according to the collected data
# you are:
# - (bull) a growth seller: you like risk and your sales are volatile wich leads to a higher growth rate
# - (bear) a defender seller: you like security and clean sales your sales are less volatile
# - moderate seller: you have a growth approach but you also like staying conservative and minimze the risks
# --- prediction ---
# predict the next turnover according to trend curves computed


from math import sqrt
from datetime import timedelta
from os import listdir
from matplotlib import pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter
from pandas import read_excel
from engine import File


class Graph:
    """Class to design graphs"""

    def __init__(self, months=False):
        self.graph_by_month = months
        self.plt = plt
        self.lang_file = File("ressources/lang/"+str(File("settings/param.json").get_dict()["lang"])+".json")

    def prepare_stats_plot(self):
        """Prepares the variables for a statistical plot"""
        self.total_turnover = []
        self.total_article_sold = []
        self.total_purchase_amount = []
        self.total_capital = []
        self.total_article_price = []
        self.min_price_article_sold = 0
        self.max_price_article_sold = 0
        self.total_untaxed = 0

    def plot_graph(self, unit_time:str, first_year:int, prev_year:int, unit_dates:list, unit_labels:list):
        """Plot the
        
        Args:
            - {str} unit_time: "months" or "trimesters"
            - {int} year: first year to start
            - {int} prev_year: year to stop
            - {list} unit_dates: list containing the dates to plot
            - {list} unit_labels: list containing the labels to plot
        """
        self.prepare_stats_plot()
        self.compute_stats_data(first_year, prev_year, unit_time)
        self.plot_data(unit_dates, unit_labels)
        self.plot_stats_infos()
        self.show()

    def standard_deviation(self, value_list:list):
        """Returns the standard deviation"""
        return sqrt(sum([(value_list[i] - sum(value_list)/len(value_list))**2 for i in range(len(value_list))])/len(value_list))
    
    def compute_stats_data(self, year:int, prev_year:int, unit_time:str):
        """Computes the statistical data
        
        Args:
            - {int} year: first year to start
            - {int} prev_year: year to stop
            - {str} unit_time: "months" or "trimesters"
        """
        accounting = self.lang_file.get_page_text("business_stats_page", "accounting")
        unit_time = self.lang_file.get_page_text("business_stats_page", unit_time)
        while not (year > prev_year):
            for i in range(len(listdir(f"{accounting}/{year}/{unit_time}"))):
                # temp variables
                current_turnover = 0
                current_total_purchase_amount = 0
                current_total_article_sold = 0
                current_total_capital = 0
                # file path
                file_name = listdir(f"{accounting}/{year}/{unit_time}")[i]
                file_path = f"{accounting}/{year}/{unit_time}/{file_name}"
                # skip the file if the month is not completed yet
                if "temp" in file_path:
                    break
                # Read the Excel file into a DataFrame
                df = read_excel(file_path)
                
                for _, row in df.iterrows():
                    amount = row["Transaction"]
                    amount = float(amount)
                    refund = row["Refund"]

                    # update min_price_article_sold
                    if refund:
                        self.total_untaxed += amount
                    if self.min_price_article_sold == 0:
                        self.min_price_article_sold = amount if (amount > 0 and not refund) else 0                    
                    elif (amount > 0 and not refund) and (amount < self.min_price_article_sold):
                        self.min_price_article_sold = amount

                    # update max_price_article_sold
                    if amount > self.max_price_article_sold and not refund:
                        self.max_price_article_sold = amount
                    current_turnover += amount if (amount > 0 and not refund) else 0
                    current_total_purchase_amount += amount if amount < 0 else 0
                    current_total_article_sold += 1 if (amount > 0 and not refund) else 0
                    current_total_capital += amount
                    if amount > 0 and not refund:
                        self.total_article_price.append(amount)

                # update the total lists
                self.total_turnover.append(current_turnover)
                self.total_purchase_amount.append(current_total_purchase_amount)
                self.total_article_sold.append(current_total_article_sold)
                self.total_capital.append(current_total_capital)

            year += 1
        
        # --- Turnover --- #
        self.total_turnover_sum = sum(self.total_turnover)
        self.avg_turnover = self.total_turnover_sum / len(self.total_turnover)
        self.min_turnover = min(self.total_turnover)
        self.max_turnover = max(self.total_turnover)
        self.std_articles_price = self.standard_deviation(self.total_article_price)
        self.average_article_price = round(self.total_turnover_sum/sum(self.total_article_sold), 2)
        self.ratio_std_articles_price = self.std_articles_price/self.average_article_price

        # --- Money spent --- #
        self.total_purchase_amount_sum = sum(self.total_purchase_amount)
        self.avg_money_spent_per_trimester = self.total_purchase_amount_sum / len(self.total_purchase_amount)
        # --- Capital --- #
        self.total_capital_sum = sum(self.total_capital)
        # round turnovers
        self.total_turnover = [round(t, 2) for t in self.total_turnover]

    def plot_data(self, unit_dates:list, unit_labels:list):
        """Plots the data on the graph
        
        
        Args:
            - {list} unit_dates: list containing the dates to plot
            - {list} unit_labels: list containing the labels to plot
        """
        self.sale_statisticals_text = self.lang_file.get_page_text("business_stats_page", "sale_statisticals")
        self.plt.figure(figsize=(12, 6), num=self.sale_statisticals_text)
        bar_width = 10*self.plt.gcf().get_size_inches()[0]/len(unit_labels)  # Adjust this value to control the space between bars
        self.plt.bar(unit_dates, self.total_turnover, width=bar_width, align='edge', color='skyblue')
        # Add turnover and trimester labels inside the bar
        for i, (date, turnover) in enumerate(zip(unit_dates, self.total_turnover)):
            # Adjust the x-position of text labels
            x_pos = date + timedelta(days=bar_width / 2)
            self.plt.text(x_pos, turnover - 7.5e-2*round(self.avg_turnover, 2), f'{turnover:,.2f}€', ha='center', fontsize=8)
            if i % 4 == 0:
                self.plt.text(x_pos, turnover - 7.5e-2*round(self.avg_turnover, 2)/2, f'{unit_labels[i]}', ha='center', fontsize=8)
            else:
                self.plt.text(x_pos, turnover - 7.5e-2*round(self.avg_turnover, 2)/2, unit_labels[i], ha='center', fontsize=8)

        # Set labels and title
        self.plt.xlabel(self.lang_file.get_page_text("business_stats_page", "x_axis_label"))
        self.plt.ylabel(self.lang_file.get_page_text("business_stats_page", "y_axis_label"))
        if not self.graph_by_month:
            self.plt.title(self.lang_file.get_page_text("business_stats_page", "title_graph_turnover_by_trimester"))
        else:
            self.plt.title(self.lang_file.get_page_text("business_stats_page", "title_graph_turnover_by_month"))            
        # Set major ticks as years and minor ticks as months
        self.plt.gca().xaxis.set_major_locator(YearLocator())
        # Format the x-axis labels to show only the year
        self.plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))

    def plot_stats_infos(self):
        """Plots the statistias sales informations on the graph"""
        self.plt.text(1.05, 0.9, self.sale_statisticals_text, ha='left', va='center', color="red", transform=plt.gca().transAxes, fontsize=14, fontweight='bold')
        total_turnover_text = self.lang_file.get_page_text("business_stats_page", "total_turnover")
        self.plt.text(1.05, 0.85, f'{total_turnover_text}{round(self.total_turnover_sum, 2):,.2f} €', ha='left', va='center', color="green", transform=plt.gca().transAxes, fontsize=12)
        untaxed_text = self.lang_file.get_page_text("business_stats_page", "untaxed")        
        self.plt.text(1.05, 0.8, f'{untaxed_text}{round(self.total_untaxed, 2):,.2f} €', ha='left', va='center', color="darkgreen", transform=plt.gca().transAxes, fontsize=12)
        average_turnover_text = self.lang_file.get_page_text("business_stats_page", "average_turnover")        
        self.plt.text(1.05, 0.75, f'{average_turnover_text}{round(self.avg_turnover, 2):,.2f} €', ha='left', va='center', color="green", transform=plt.gca().transAxes, fontsize=12)
        max_turnover_text = self.lang_file.get_page_text("business_stats_page", "max_turnover")        
        self.plt.text(1.05, 0.7, f'{max_turnover_text}{round(self.max_turnover, 2):,.2f} €', ha='left', va='center', color="green", transform=plt.gca().transAxes, fontsize=12)
        min_turnover_text = self.lang_file.get_page_text("business_stats_page", "min_turnover")        
        self.plt.text(1.05, 0.65, f'{min_turnover_text}{round(self.min_turnover, 2):,.2f} €', ha='left', va='center', color="green", transform=plt.gca().transAxes, fontsize=12)
        most_expensive_article_text = self.lang_file.get_page_text("business_stats_page", "most_expensive_article")
        self.plt.text(1.05, 0.6, f'{most_expensive_article_text}{self.max_price_article_sold:,.2f} €', ha='left', va='center', color="purple", transform=plt.gca().transAxes, fontsize=12)
        cheapest_article_text = self.lang_file.get_page_text("business_stats_page", "cheapest_article")
        self.plt.text(1.05, 0.55, f'{cheapest_article_text}{self.min_price_article_sold:,.2f} €', ha='left', va='center', color="purple", transform=plt.gca().transAxes, fontsize=12)
        total_articles_sold_text = self.lang_file.get_page_text("business_stats_page", "total_articles_sold")
        self.plt.text(1.05, 0.5, f'{total_articles_sold_text}{sum(self.total_article_sold)}', ha='left', va='center', color="darkorange", transform=plt.gca().transAxes, fontsize=12)
        average_articles_sold_text = self.lang_file.get_page_text("business_stats_page", "average_articles_sold")
        self.plt.text(1.05, 0.45, f'{average_articles_sold_text}{int(sum(self.total_article_sold)/len(self.total_article_sold))}', ha='left', va='center', color="darkorange", transform=plt.gca().transAxes, fontsize=12)
        average_article_price_text = self.lang_file.get_page_text("business_stats_page", "average_article_price")
        self.plt.text(1.05, 0.4, f'{average_article_price_text}{self.average_article_price:,.2f} €', ha='left', va='center', color="darkorange", transform=plt.gca().transAxes, fontsize=12)
        total_money_spent_text = self.lang_file.get_page_text("business_stats_page", "total_money_spent")
        self.plt.text(1.05, 0.35, f'{total_money_spent_text}{round(self.total_purchase_amount_sum, 2):,.2f} €', ha='left', va='center', color="blue", transform=plt.gca().transAxes, fontsize=12)
        average_money_spent_text = self.lang_file.get_page_text("business_stats_page", "average_money_spent")
        self.plt.text(1.05, 0.3, f'{average_money_spent_text}{round(self.avg_money_spent_per_trimester, 2):,.2f} €', ha='left', va='center', color="blue", transform=plt.gca().transAxes, fontsize=12)        
        # --- Standard deviation presentation --- #        
        std_pres_sentence = self.lang_file.get_page_text("business_stats_page", "std_pres_sentence")        
        self.plt.text(1.05, 0.25, f'{std_pres_sentence} {round(self.std_articles_price, 2):,.2f} €', ha='left', va='center', color="darkcyan", transform=plt.gca().transAxes, fontsize=8)        
        # explanations
        if self.ratio_std_articles_price < 0.2:
            std_explanation = self.lang_file.get_page_text("business_stats_page", "consistent_prices")
        elif self.ratio_std_articles_price > 0.5:
            std_explanation = self.lang_file.get_page_text("business_stats_page", "wide_range_pries")
        else:
            std_explanation = self.lang_file.get_page_text("business_stats_page", "varying_prices")
        self.plt.text(1.05, 0.2, f'{std_explanation}', ha='left', va='center', color="darkcyan", transform=plt.gca().transAxes, fontsize=8)
        # --- Net capital of the company --- #
        capital_text = self.lang_file.get_page_text("business_stats_page", "capital")        
        self.plt.text(1.05, 0.15, f'{capital_text}{round(self.total_capital_sum, 2):,.2f} €', ha='left', va='center', color="red", transform=plt.gca().transAxes, fontsize=12)       

    def show(self):
        """Shows the plot"""
        self.plt.tight_layout()
        self.plt.show()