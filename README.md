# Nasdaq 100 Stock Prices Web Scraper

This project is a Python-based web scraper that automatically retrieves the daily closing prices of the largest companies listed on the Nasdaq 100 index. The data is scraped from [Markets Insider Nasdaq 100 Components](https://markets.businessinsider.com/index/components/nasdaq_100) and is then written to a Google Spreadsheet for easy access and analysis. [Click](https://docs.google.com/spreadsheets/d/1_DReqeQ5haLU_CNjYo-t9tclTaCaE40tYkkIvocnvtQ/edit?gid=0#gid=0) to reach the spreadsheet.

![Project Screenshot](image.png)

## Features
- **Automated Stock Price Retrieval**: Scrapes daily closing prices of Nasdaq 100 companies from the specified website.
- **Google Sheets Integration**: Writes the scraped data directly into a Google Spreadsheet.
- **Daily Automation**: Can be scheduled to run daily to fetch the latest data.
- **Secure Google OAuth Authentication**: Uses OAuth2 for secure access to your Google Sheets.

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: Web scraping tool used to navigate and extract data from the website.
- **gspread**: Python library for interacting with Google Sheets API.
- **Google OAuth2**: Secure authentication for accessing Google Sheets.

## Requirements

Before setting up and running the project, ensure you have the following:

- **Python 3.12**: You can download it from [python.org](https://www.python.org/downloads/).
- **Google Account**: To access and write data to a Google Spreadsheet.
- **Browser Driver**: Chromium browser installed for Selenium.
- **Docker (Optional)**: Docker and docker compose to run program on docker. 

## Setup Instructions

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/alikilicw/nasdaq-stock-prices.git
```

### 2. Install Dependencies
If you will use Docker to run the program, you can pass this step.
```bash
pip install -r requirements.txt
```

### 3. Create a Google API Project and Credentials

- Go to [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
- Enable the Google Sheets API and Google Drive API.
- Create OAuth2 credentials and download the `credentials.json` file.
- Move the `credentials.json` file into your project directory.

### 4. Create and Share a Google Spreadsheet

- Create a new Google Spreadsheet in your Google Drive.
- Open the `credentials.json` file and find the `client_email` field.
- Share the newly created Google Spreadsheet with this `client_email` (it will look like `your-project-id@developer.gserviceaccount.com`).

### 5. Update the Env File

- Create an .env file in your project directory.
    - `WORKBOOK_ID`: Spreadsheet id. You can find that id in your spreadsheet url. (looks like `1_DReqeW5haLU_ANjYo-t9tklTaCaE40TYkkIvocnftQ`)
    - `DRIVER_LOCATION`: Chromium driver location in your machine.
    - `SCHEDULER_HOUR`: At what hour does the scheduler run? (You can adjust it to 21 for Nasdaq close time.)
    - `SCHEDULER_MINUTE`: At what minute does the scheduler run?

### 6. Run the Program

For python:
```bash
python main.py
```

For docker:
```bash
docker compose up --build -d
```

### This project is developed by [github:alikilicw].