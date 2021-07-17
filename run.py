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
year = datetime.date.today().year
now = datetime.datetime.utcnow().isoformat() + 'Z'
GMT_OFF = '+02:00'


def welcome_screen():
    """
    The patient or staff member is greeted with this welcome screen,
    from here users can either choose the patient or staff section.
    """
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
    """
    This is the staff area, from which staff members can access, change
    or delete patient data after successfully entering the password.
    """
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
            get_appointments(now, future_date(14))
            break

        elif password_entered in ('e', 'E'):
            welcome_screen()
            break

        else:
            print('\nWrong password, please try again\n')
            attempts += 1


def get_appointments(earliest, latest):
    """
    Get appointments for the given period
    """
    print('Here are the one hour scheduled appointments:\n')
    now = datetime.datetime.now().isoformat()
    now = now + 'Z'

    events_result = CAL.events().list(  # pylint: disable=maybe-no-member
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
        start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S' + GMT_OFF)
        start = start.strftime("%H:%M, %dth %b %Y")

        print(start, event['summary'], event['description'])
        # print(start, event['summary'])


# def find_free_time():


def suggest_appointment():
    """
    Function to let patient continue with booking or go back,
    for example if a staff  member entered the wrong input.
    """

    print("Let's find you an appointment.\n")
    print('Press "1" to continue or "e" to exit.\n')
    book_or_back = input()

    while True:

        if book_or_back == '1':
            book_appointment(year)
            break

        elif book_or_back == 'e' or 'E':
            welcome_screen()
            break
        else:
            print('Invalid entry, try again\n')


def future_date(day):
    """
    Function to let patient continue with booking or go back,
    for example if a staff  member entered the wrong input.

    @param day (int): The amount of days from now into the future to
    pass into the function
    """

    date = datetime.datetime.now() + timedelta(day)
    date = date.isoformat() + 'Z'
    return date


def days_feb():
    """
    Simple function to calculate amount of days in Feb on the
    year the request is made.
    """

    d = 28

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                d = 29
            else:
                d = 28
        else:
            d = 29
    else:
        d = 28

    return d

def book_appointment(year):
    """
    Gets information from user to determine date and time for appointment.

    @param year(int): the year of the appointment.
    """

    month_dict = {
        'Jan': 31,
        'Feb': days_feb(),
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'Jun': 30,
        'Jul': 31,
        'Aug': 31,
        'Sep': 30,
        'Okt': 31,
        'Nov': 30,
        'Dec': 31,
    }

    while True:

        print('Which month would you would like to come?\n')
        month = input('(3 letters, 1st capital)\n')

        try:
            if month in month_dict.keys():

                int_month = datetime.datetime.strptime(month, '%b')
                int_month = int_month.strftime('%m')
                int_month = int(int_month)

                this_month = datetime.datetime.now().month
                int_this_month = int(this_month)

                if int_month < int_this_month:
                    year = datetime.datetime.today() + timedelta(365.2425)
                    year = year.year

                print(f'{month}, {year}. Which date?\n')
                date = input('1 - 31:\n')
                if int(date) > 31 or int(date) < 1 or
                    (month == 'Feb' and int(date) > days_feb()):
                    raise ValueError('date not valid, try again')

                print('What time?\n')
                hour = input('Enter hour, 9 - 17:\n')

                apntmnt_time = (f'{hour}:00, {date}th {month} {year}')
                apntmnt_time = datetime.datetime.strptime(
                    apntmnt_time, '%H:%M, %dth %b %Y'
                )

                end_time = apntmnt_time + timedelta(hours=+1)
                apntmnt_time = apntmnt_time.strftime('%Y-%m-%dT%H:%M:%S' + GMT_OFF)
                end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S' + GMT_OFF)

                name = input('enter your full name:\n')

                email = input('enter your email:\n')

                details = input('discribe your symptoms:\n')

                print(f'Confirm appointment: {apntmnt_time}?')
                confirm = input('"y" = YES, "n" = NO\n')
                if confirm == 'y':
                    new_event(apntmnt_time, end_time, name, email, details)
                    return False

            else:
                raise ValueError
        except ValueError:
            print('Month incorrect, please try again\n')


def new_event(start, end, name, email, details):
    """
    Makes an event entry in Google Calendar, getting data from
    the book_appointment function.

    @param start(str): Start time of appointment
    @param end(str): Start time of appointment
    @param name(str): Name entered by patient
    @param email(str): Email entered by patient
    @param details(str): Description of symptoms entered by patient
    """

    EVENT = {
        "start": {
            "dateTime": start,
            },
        "end": {
            "dateTime": end,
            },
        'summary': name,
        'description': f'{email}, {details}'
    }

    e = CAL.events().insert(  # pylint: disable=maybe-no-member
            calendarId=CAL_ID,
            sendNotifications=True, body=EVENT).execute()

    print(f'Thanks, {name}, appointment added:\n')
    print(f'{start}, {email}')
    print(details)
    goback = input('Press any key to go back to the beginning\n')

    if goback != '¶':
        welcome_screen()

        # Start: %s End: %s' % (
        # e['summary'].encode('utf-8'), e['start']
        # ['dateTime'], e['end']['dateTime'])


# suggest_appointment()
# get_appointments()
welcome_screen()


# def show_schedule(CAL):
#     """
#     Shows the schedule if password has been entered correctly.
#     """
#     # Call the Calendar API
#     events_result = CAL.events().list(
#         calendarId=CAL_ID,
#         timeMin=now,
#         maxResults=10, singleEvents=True,
#         orderBy='startTime'
#     ).execute()

#     events = events_result.get('items', [])

#     if not events:
#         print('No upcoming events found.')
#     for event in events:

#         start = event['start'].get('dateTime', event['start'].get('date'))
#         start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
#         start = start.strftime("%H:%M, %dth %b %Y")
#         print(start, event['summary'])