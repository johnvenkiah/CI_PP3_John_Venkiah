from __future__ import print_function
import stdiomask
import password
import datetime
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = 'http://www.googleapis.com/auth/calendar'
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
CAL = build('calendar', 'v3', credentials=CREDS)
CAL_ID = 'uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com'

GMT_OFF = '+02:00'


def welcome_screen():
    welcome_greeting = 'Welcome to the Feelgood Physio booking system\n'
    print(staff_greeting.upper())

    while True:

        staff_or_customer = input('\nPress "b" to book an appointment or "s" for staff login:\n')
        staff_or_customer.lower()

        

def staff_login(password):
    attempts = 0
    staff_greeting = 'Feelgood Physio - Staff login area\n'
    print(staff_greeting.upper())

    while True:

        password_entered = stdiomask.getpass('Enter your password:\n\n')

        if attempts == 4:
            print('\nToo many incorrect attempts, exiting...\n')
            break

        if password_entered == password.password:
            print('\nPassword correct, here is your schedule:\n')
            show_schedule(CAL)
            break

        else:
            print('\nWrong password, please try again\n')
            attempts += 1


def show_schedule(CAL):
    """
    Shows the schedule if password has been entered correctly.
    """

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = CAL.events().list(
        calendarId=CAL_ID,
        timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:

        start = event['start'].get('dateTime', event['start'].get('date'))
        start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
        start = start.strftime("%H:%M, %dth %b %Y")
        print(start, event['summary'])


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


staff_login(password)
