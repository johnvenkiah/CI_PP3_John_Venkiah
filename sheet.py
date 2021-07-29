"""
Sheet file, functions to read and update Google Sheets on Google Drive.
"""

import gspread
from google.oauth2.service_account import Credentials

"""
IMPORTS

gspread: Make it possible to send and recieve data to a Google spreadsheet.

Credentials from google.oauth2.service_account: The credentials for the Google
Account accessing the data.
"""

"""
SCOPED_SHEETS, CREDS, SCOPED_CREDS: used with Google API Client to gain access to
and modify data on and Google Sheets. Some help here from the walkthrough
project Love Sandwiches.
"""
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

        #  Get list of all values in spreadsheet
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

    #  add each row to the p_dict dictionary and display them to user
    for row in p_data:
        if p_data[0] == row:
            continue

        #  zip method: credit to this on Stack Overflow:
        #  https://stackoverflow.com/questions/209840/
        #  how-do-i-convert-two-lists-into-a-dictionary
        p_dict = dict(zip(p_data[0], row))

        #  Replace characters so string is displayed more readable 
        print(
            '\n' + str(p_dict).replace('{', '').replace(
                '}', '').replace("'", '')
        )


def get_p_nr():
    """
    Assigns a new patient number to patient before adding it to patient log.
    """

    #  Get the log list
    p_data = get_p_log()

    #  Assign patient nr to 1 if there are no patients
    if p_data[-1][0] == 'Patient nr':
        p_nr = 1
    else:

    #  Get the last patent nr cell and give it the number next in line
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

    #  Add new row if user exists in log
    if name not in str(pat_log.col_values(2)):
        p_nr = get_p_nr()

    #  Use the g.sheets append_row method to append the new patient data
    #  to Google sheet
        data = [p_nr, name, email, details]
        pat_log.append_row(data)

    else:

        #  If not, edit the email and symptoms of that patient
        for row in pat_log.col_values(2):
            if name in row:
                row_nr = pat_log.find(name).row

                #  Update the details cell
                pat_log.update_cell(row_nr, 4, details)
