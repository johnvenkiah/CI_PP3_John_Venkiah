from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from google.oauth2.service_account import Credentials

SCOPES = 'http://www.googleapis.com/auth/calendar'
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
CAL = build('calendar', 'v3', credentials=CREDS)

GMT_OFF = '-00:00' #GMT
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
