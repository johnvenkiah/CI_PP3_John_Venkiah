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


def get_p_data(p_log):
    p_log_dict = {}
    p_dict = {}
    p_data = p_log.get_all_values()
    for row in p_data:
        if p_data[0] == row:
            continue
        p_dict = dict(zip(p_data[0], row))
        p_log_dict = p_log_dict, p_dict

    print('\n' + str(p_log_dict).replace(
        "{", "").replace("}", "").replace("'", "").replace(
        "(", "").replace(")", "").replace(",", "")
    )


# def append_p_row(p_log):

# get_p_data(p_log)


