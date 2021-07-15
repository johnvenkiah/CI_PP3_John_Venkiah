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

GMT_OFF = '-00:00'


def staff_login(password):
    attempts = 0

    while True:
        print('Customer login area\n')

        password_entered = stdiomask.getpass('Enter your password:\n')

        if attempts == 4:
            print('Too many incorrect attempts, exiting...\n')
            break

        if password_entered == password.password:
            print('Password correct, here is your schedule:\n')
            show_schedule(CAL)
            break

        else:
            print('Wrong password, please try again\n')
            attempts += 1


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

    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))  # 'date' needed?
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
