import gspread, os
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

scopes = [
    'https://www.googleapis.com/auth/spreadsheets'
]

# authorization
creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
client = gspread.authorize(creds)

WORKBOOK_ID = os.getenv('WORKBOOK_ID')

# get a workbook instance
def get_workbook():
    workbook = client.open_by_key(WORKBOOK_ID)
    return workbook
