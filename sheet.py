import gspread
from google.oauth2.service_account import Credentials

SCOPES_SHEETS = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES_SHEETS)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('feelgood_patient_data')

p_log = SHEET.worksheet('patient_log')
p_data = p_log.get_all_values()

def get_p_data(p_log):
    p_dict = {}

    for row in p_data:
        if p_data[0] == row:
            continue
        p_dict = dict(zip(p_data[0], row))
        print(
            str(p_dict).replace("{", "").replace(
                "}", "").replace("'", "")
        )

def get_p_nr(p_log):
    if not p_data:
        p_nr = 1
    else:
        p_nr = int(p_data[-1][0]) + 1
    return str(p_nr)