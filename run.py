from __future__ import print_function
import stdiomask
import password
import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = 'http://www.googleapis.com/auth/calendar'
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
CAL = build('calendar', 'v3', credentials=CREDS)
CAL_ID = 'uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com'
now = datetime.datetime.utcnow().isoformat() + 'Z'
GMT_OFF = '+02:00'


def welcome_screen():
    welcome_greeting = 'Welcome to the Feelgood Physio booking system\n'
    print(welcome_greeting.upper())

    while True:

        staff_or_customer = input(
            '\nPress "b" to book an appointment or "s" for staff login:\n'
            )
        staff_or_customer = staff_or_customer.lower()
        if staff_or_customer == 's':
            staff_login(password)
            break

        elif staff_or_customer == 'b':
            suggest_appointment()
            break

        else:
            print('\nInvalid entry, please try again\n')


def staff_login(password):
    attempts = 0
    staff_greeting = 'Feelgood Physio - Staff login area\n'
    print(staff_greeting.upper())

    while True:

        password_entered = stdiomask.getpass(
            'Enter your password or "e" to exit:\n\n'
            )

        if attempts == 4:
            print('\nToo many incorrect attempts, exiting...\n')
            break

        if password_entered == password.password:
            print('\nPassword correct, here is your schedule:\n')
            show_schedule(CAL)
            break

        elif password_entered in ('e', 'E'):
            welcome_screen()
            break

        else:
            print('\nWrong password, please try again\n')
            attempts += 1


def show_schedule(CAL):
    """
    Shows the schedule if password has been entered correctly.
    """
    # Call the Calendar API
    events_result = CAL.events().list(
        calendarId=CAL_ID,
        timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:

        start = event['start'].get('dateTime', event['start'].get('date'))
        start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
        start = start.strftime("%H:%M, %dth %b %Y")
        print(start, event['summary'])


def get_appointments(earliest, latest):
    """
    Get appointments for the given period
    """
    print('Here are the one hour scheduled appointments:\n')
    now = datetime.datetime.now().isoformat()
    now = now + 'Z'

    events_result = CAL.events().list(
        calendarId=CAL_ID,
        timeMin=earliest,
        timeMax=latest,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:

        start = event['start'].get('dateTime')
        start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
        start = start.strftime("%H:%M, %dth %b %Y")

        print(start, event['summary'])


# def find_free_time():


def suggest_appointment():

    print('When would you like an appointment?\n')
    print('Within a week: "1"\n')
    print('Within two weeks: "2"\n')
    print('Choose date: "3"\n')
    print('Press "e" to exit')
    apntmt_choice = input()

    while True:

        if apntmt_choice == '1':
            get_appointments(now, future_date(7))
            break

        elif apntmt_choice == '2':
            get_appointments(future_date(7), future_date(14))
            break

        elif apntmt_choice == '3':
            get_appointments(now, future_date(61))
            break

        elif apntmt_choice == 'e' or 'E':
            welcome_screen()
            break
    else:
        print('Invalid entry, try again\n')


def future_date(day):
    date = datetime.datetime.now() + timedelta(day)
    date = date.isoformat() + 'Z'
    return date


def new_event(CAL):
    """
    New event in Google Calendar.
    """
    EVENT = {
        "start": {
            "dateTime": '2021-07-22T15:00:00Z',
            },
        "end": {
            "dateTime": '2021-07-22T16:00:00Z',
            },
        'summary': 'John Locke, Neckpain',
    }

    e = CAL.events().insert(
            calendarId=CAL_ID,
            sendNotifications=True, body=EVENT).execute()

    print(
        '''*** %r event added:
        Start: %s End: %s''' % (
            e['summary'].encode('utf-8'), e['start']
            ['dateTime'], e['end']['dateTime'])
    )


suggest_appointment()
# get_appointments()
# welcome_screen()
