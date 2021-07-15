from __future__ import print_function
import datetime
from googleapiclient.discovery import build
# from httplib2 import Http
from google.oauth2.service_account import Credentials
import password

SCOPES = 'http://www.googleapis.com/auth/calendar'
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
CAL = build('calendar', 'v3', credentials=CREDS)

GMT_OFF = '-00:00'


def staff_login(password):
    while True:
        print('Customer login area\n')

        password_entered = input('Enter your password:\n')

        if validate_password(password_entered):
            print('Password correct, here is your schedule:\n')
            show_schedule(CAL)
            break


def validate_password(password_entered):
    """
    Checks if the user has the correct password to enter.
    If so, show show schedule will execute.
    """
    try:
        if password_entered == '':
            raise ValueError('No password entered, please try again.\n')

    except ValueError:
        if password_entered != password.password:
            print('Wrong password, please try again\n')
            return False

    return True


def show_schedule(CAL):
    """
    Shows the schedule if password has been entered correctly.
    """

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = CAL.events().list(
        calendarId='uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com',
        timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    events_result = CAL.events().list(
        calendarId='uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com',
        timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
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
            calendarId='uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com',
            sendNotifications=True, body=EVENT).execute()

    print(
        '''*** %r event added:
        Start: %s End: %s''' % (
            e['summary'].encode('utf-8'), e['start']
            ['dateTime'], e['end']['dateTime'])
    )


staff_login(password)
