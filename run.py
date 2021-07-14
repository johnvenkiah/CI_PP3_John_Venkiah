from __future__ import print_function
import datetime
from apiclient.discovery import build
from httplib2 import Http
from google.oauth2.service_account import Credentials

SCOPES = 'http://www.googleapis.com/auth/calendar'
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
CAL = build('calendar', 'v3', credentials=CREDS)

GMT_OFF = '-00:00'
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

print('''*** %r event added:
    Start: %s
    End: %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = CAL.events().list(
    calendarId='uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com', timeMin=now,
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
