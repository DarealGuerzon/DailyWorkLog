import gspread
from pathlib import Path

CREDENTIALS_PATH = Path(__file__).parent / "credentials.json"

SHEET_NAME = "Work Log"

def main():
    print("Authenticating with Google Sheets...")
    gc = gspread.service_account(filename=str(CREDENTIALS_PATH))

    print(f"Opening the sheet: {SHEET_NAME}")
    sh = gc.open(SHEET_NAME).sheet1

    print("Appending a new row...")
    sh.append_row(["Test Entry", "This is a test log entry."])

    print("Row appended successfully.")

if __name__ == "__main__":
    main()

# This script tests the connection to Google Sheets and appends a test row.