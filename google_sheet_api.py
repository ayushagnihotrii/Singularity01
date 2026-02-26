# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# def write_data_to_sheet(ip_address, timestamp):
#     scope = [
#         "https://spreadsheets.google.com/feeds",
#         "https://www.googleapis.com/auth/drive"
#     ]

#     credentials = ServiceAccountCredentials.from_json_keyfile_name(
#         "singularity01-488606-13f2241498c5.json",
#         scope
#     )

#     client = gspread.authorize(credentials)

#     sheet = client.open("singularity01").sheet1

#     current_rows = len(sheet.get_all_values())
#     serial_number = current_rows  # row 1 is header

#     sheet.append_row([serial_number, timestamp, ip_address])

import os
import json
import gspread
from google.oauth2 import service_account

google_creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])

credentials = service_account.Credentials.from_service_account_info(
    google_creds
)

client = gspread.authorize(credentials)