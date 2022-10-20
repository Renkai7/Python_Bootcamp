import os
import requests

# CONSTANTS
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
SHEET_NAME = "prices"
SHEETSON_API_KEY = os.environ.get("SHEETSON_API_KEY")

# Endpoints
sheetson_endpoint = f"https://api.sheetson.com/v2/sheets/{SHEET_NAME}"

# Headers
sheetson_headers = {
    "Authorization": f"Bearer {SHEETSON_API_KEY}",
    "X-Spreadsheet-Id": SPREADSHEET_ID,
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_sheet(self):
        sheet_response = requests.get(url=sheetson_endpoint, headers=sheetson_headers)
        data = sheet_response.json()
        self.sheet_data = data["results"]

        return self.sheet_data

    # Check for changes in Sheet data and update Google Sheets
    def update_sheet(self):
        for data in self.sheet_data:
            sheet_params = {
                "IATA Code": data["IATA Code"]
            }
            sheet_update = requests.put(url=f"{sheetson_endpoint}/{data['rowIndex']}", json=sheet_params,
                                        headers=sheetson_headers)
