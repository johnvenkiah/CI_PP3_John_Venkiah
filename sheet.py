"""
SHEET FILE, functions to read and update Google Sheets on Google Drive
"""

import gspread
from google.oauth2.service_account import Credentials

SCOPES_SHEETS = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES_SHEETS)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('feelgood_patient_data')
pat_log = SHEET.worksheet('patient_log')


def get_p_log():
    """
    Gets the patient log from Google sheets worksheet and passes it
    to show_p_data. Get all values methods from the Google Resources
    website: https://developers.google.com/sheets
    """
    try:
        p_data = pat_log.get_all_values()

        return p_data

    except Exception as error:  # pylint: disable=broad-except
        print(f'could not load Google worksheet, probable API error: {error}')
        return False


def show_p_data():
    """
    Gets and shows all entries in patient log, which is a Google Sheet stored
    on Google Drive.
    """
    p_data = get_p_log()
    p_dict = {}

    for row in p_data:
        if p_data[0] == row:
            continue
        p_dict = dict(zip(p_data[0], row))
        print(
            '\n' + str(p_dict).replace('{', '').replace(
                '}', '').replace("'", '')
        )


def get_p_nr():
    """
    Assigns a new patient number to patient before adding it to patient log.
    """

    p_data = get_p_log()
    if p_data[-1][0] == 'Patient nr':
        p_nr = 1
    else:
        p_nr = int(p_data[-1][0]) + 1
    return str(p_nr)


def append_p_row(name, email, details):
    """
    Adds a new patient row with details to log on Google Sheets. If patient
    name already exists, only updates the symptoms, stored in details variable.
    @para, name(str): Name from user input
    @para, email(str): Email from user input
    @para, details(str): Symptoms (details var.) from user input
    """

    if name not in str(pat_log.col_values(2)):
        p_nr = get_p_nr()

        data = [p_nr, name, email, details]
        print(data)
        print(p_nr)
        pat_log.append_row(data)

    else:
        for row in pat_log.col_values(2):
            if name in row:
                row_nr = pat_log.find(name).row
                pat_log.update_cell(row_nr, 4, details)
