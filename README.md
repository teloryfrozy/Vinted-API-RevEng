# Vinted-API-RevEng Repository

# Project Setup Guide

## Prerequisites
- This project is optimized for Windows; icons may not display correctly on other platforms.
- Ensure you have Python installed.

## Installation
1. Install project dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
1. Open the root folder in Visual Studio Code (VSC).
2. Navigate to the `gui/py` directory.
3. Run the `launcher.py` file to start the application.


# Note of the Creator (02/01/2024)

## Project Timeline

- **Start project:** 02/2023
- **API Rev:** 06/2023
- **End project:** 08/2023


This project was stopped when it was found to involve unauthorized data retrieval, including user addresses and gender information, which isn't allowed by default.

There are tools that simulate clicking actions on behalf of a user (they are all illegal). By the way, all Discord bot scrapers for ads are also illegal.

This is where I began initially. Then, I discovered that Vinted had an API. Initially unsuccessful, I revisited the project a couple of weeks/months later, using Man-in-the-Middle software. I spent two months comprehensively understanding everything, especially the authentication process.

# This code and engineering could potentially be used to create a business that Vinted might consider paying for, as it offers significant time-saving benefits

I chose not to proceed further because I don't want to earn money in that manner, even though it could generate passive income and create job opportunities. I reached out to developers from the Vinted team, and my goal for the upcoming years is to get a job at Vinted, as it's one of my dream companies. I wish I could implement some features into the official app

Vinted stores the access token in a cookie. This is why the app operates for a limited time, requiring the user to copy their access token again, as the refresh token isn't stored on the client side due to security reasons.

This project improved my skills. If I did it again, I'd aim to use more powerful tools like Git, Django, and a JS framework for the frontend to work faster. I'd focus on creating a secure online service. Now, I have a better understanding of API authentication.


# Project Considerations 💡

- Use a dedicated email address for Vinted to avoid issues with other emails.

## TODOs

### Frontend:
- Implement a website using a framework for an updated and visually appealing interface.
- Develop a subscriber messaging feature (e.g., promo examples).
- Design a custom thank-you message interface based on the buyer's gender.
- Create a customizable feedback page template with the ability to add various custom messages based on time (day or evening) and user's gender.
- Establish a pop-up notification linked to the database, signaling low stock of a product, with an option to update stock status within the app.

### Backend:
- Create a database.
- Utilize a framework like Django.
- Develop a publication menu linked to the database (search bar with ad titles, NEW Article => Add to the database (optional but checked by default)).
- Enable 5 favorite messages that can be easily copied by clicking a button.
- Create a feature for an annual report compatible each year.


### Client App:
- Build a desktop application specifically for printing file.

-----------------------------------
## Application Features
-----------------------------------

### Developed Features 🚀

#### Vinted Features:
- Automatic retrieval of Vinted shipping labels.
- Addition of customizable thank-you messages on a blank section of the shipping label.
- Automatic message when a buyer purchases an item.
- Auto-delete conversation if no messages for x months.
- Random auto leave feedbacks.
- Auto-send notifications to users who liked an item.
- Database of items for quick reuploading of templates for items you have multiple copies of.
- Auto print of shipping labels automatically (Adobe Reader installed needed).
- Auto accounting: exportation of all transactions and generation of a graph & stats about sales & visualization of data.

#### Mail Management:
- Auto-delete notification emails.
- Automated sorting based on their source (LebonCoin, Vinted, Carriers, ...).

#### In Development:
- Ad refresh (working but limited by server-side request limits) so the number of refreshed ads is restricted per access token.