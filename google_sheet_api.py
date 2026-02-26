import os
import json
import gspread
from google.oauth2 import service_account

SHEET_NAME = "singularity01"

_client = None


def _get_client():
    global _client
    if _client is None:
        google_creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        credentials = service_account.Credentials.from_service_account_info(
            google_creds,
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]
        )
        _client = gspread.authorize(credentials)
    return _client


def write_data_to_sheet(ip_address, timestamp):
    client = _get_client()
    sheet = client.open(SHEET_NAME).sheet1

    # Count rows to generate serial number
    current_rows = len(sheet.get_all_values())
    serial_no = current_rows  # header already occupies row 1

    sheet.append_row([serial_no, timestamp, ip_address])
