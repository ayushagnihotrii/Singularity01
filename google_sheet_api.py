import os
import json
import gspread
from google.oauth2 import service_account

google_creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])

credentials = service_account.Credentials.from_service_account_info(
    google_creds,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

client = gspread.authorize(credentials)

SHEET_NAME = "singularity01"

def write_data_to_sheet(ip_address, timestamp):
    sheet = client.open(SHEET_NAME).sheet1
    sheet.append_row([ip_address, timestamp])
