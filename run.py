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
GMT_OFF = '+01:00'


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
            return False

        elif staff_or_customer == 'b':
            suggest_appointment()
            return False

        else:
            print('\nInvalid entry, please try again\n')


def suggest_appointment():
    """
    Function to let patient continue with booking or go back,
    for example if a staff  member entered the wrong input.
    """

    print("Let's find you an appointment.\n")
    book_or_back = input(
        'Press "1" to continue or any other key to go back.\n'
        )

    if book_or_back == '1':
        get_month(year)

    else:
        welcome_screen()


def e_to_exit(user_input):
    """
    Gets user back to welcome screen if they input "e".
    @paran user_input(str): input from user.
    """

    if user_input.lower() == 'e':
        welcome_screen()
        return False


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

        e_to_exit(password_entered)

        if attempts == 4:
            print('\nToo many incorrect attempts, exiting...\n')
            return False

        if password_entered == password.password:
            print('\nPassword correct, here is your schedule:\n')
            get_appointments(now, future_date(14))
            print_appointments()
            break

        else:
            print('\nWrong password, please try again\n')
            attempts += 1


def get_appointments(earliest, latest):
    """
    Get scheduled appointments for the given period from the Google Calendar

    @param earliest(str): starttime for period.
    @param latest(str): endtime for period.
    """

    print('\nChecking schedule...\n')
    now = datetime.datetime.now().isoformat()
    now = now + 'Z'

    events_result = CAL.events().list(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        timeMin=earliest,
        timeMax=latest,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    global events
    events = events_result.get('items', [])

    return events


def print_appointments():
    """
    Print the events taken through the get_appointments function.

    @param earliest(str): starttime for period.
    @param latest(str): endtime for period.
    """

    if not events:
        print('No upcoming events found.')
    for event in events:

        start = event['start'].get('dateTime')
        start = datetime.datetime.strptime(
            start, '%Y-%m-%dT%H:%M:%S' + GMT_OFF
        )
        start = start.strftime("%H:%M, %dth %b %Y")

        print(start, event['summary'], event['description'])
        # print(start, event['summary'])


def future_date(day):
    """
    Gives a day in the future in datetime format depending on day parameter.

    @param day (int): Amount of days from now into the future to return.
    """

    date = datetime.datetime.now() + timedelta(day)
    date = date.isoformat() + 'Z'
    return date


def days_feb():
    """
    Simple function to calculate amount of days in Feb on the
    year the request is made.
    """

    d = 29 if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0) else 28
    return d


def get_month(year):
    """
    Initiate the booking process and gets month from user for appointment.

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
        month = input('3 letters, first capital. "e" to exit.\n')
        days_in_month = month_dict.get(month)

        e_to_exit(month)

        if month in month_dict.keys():

            int_month = datetime.datetime.strptime(month, '%b')
            int_month = int_month.strftime('%m')
            int_month = int(int_month)

            this_month = datetime.datetime.now().month
            int_this_month = int(this_month)

            if int_month < int_this_month:
                year = datetime.datetime.today() + timedelta(365.2425)
                year = year.year

            get_date(days_in_month, month, year)
            return False

        elif month.isnumeric():
            print('Month incorrect, please try again\n')
        else:
            print('Month incorrect, please try again\n')


def get_date(days_in_month, month, year):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param month(str): Month given by user
    @param year(str): Year given by user
    """

    while True:

        print(f'{month}, {year}. Which date?\n')
        date = input('Enter two digits, "e" to exit.:\n')

        e_to_exit(date)

        if (
            date.isnumeric() and
            int(date) <= int(days_in_month) and
            int(date) > 0
        ):
            get_time(date, month, year)
            return False
        else:
            print('Date incorrect, please try again\n')


def get_time(date, month, year):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param month(str): Month given by user
    @param year(str): Year given by user
    """
    while True:

        print(f'{date} {month}, {year}. What time?\n')
        hour = input('Enter hour, 9 - 17. "e" to exit.\n')

        e_to_exit(hour)

        if hour.isnumeric() and int(hour) >= 9 and int(hour) < 17:

            apntmnt_time = (f'{hour}:00, {date} {month} {year}')
            apntmnt_time = datetime.datetime.strptime(
                apntmnt_time, '%H:%M, %d %b %Y'
            )

            end_time = apntmnt_time + timedelta(hours=+1)
            apntmnt_time = apntmnt_time.strftime(
                '%Y-%m-%dT%H:%M:%S' + GMT_OFF
            )
            end_time = end_time.strftime(
                '%Y-%m-%dT%H:%M:%S' + GMT_OFF
            )

            get_appointments(apntmnt_time, end_time)

            if events:
                print('Time fully booked, choose another time.\n')
            else:
                print(f'{hour}:00 on {date} {month}, {year} is free.\n')
                enter_details(apntmnt_time, end_time)
                return False
        else:
            print('Sorry, invalid entry.\n')


def enter_details(apntmnt_time, end_time):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param start(str): Start time of appointment
    @param end(str): Start time of appointment
    """

    while True:

        name = input('Enter your full name ("e" to exit):\n')
        e_to_exit(name)

        email = input('Enter your email:\n')
        e_to_exit(email)

        details = input('Shortly describe your symptoms ("e" to exit):\n')
        e_to_exit(details)

        print(f'Confirm appointment: {apntmnt_time}?')
        confirm = input('"y" = YES, "n" = NO\n')
        if confirm == 'y':
            new_event(
                apntmnt_time, end_time, name, email, details
            )
            return False

        else:
            print('Lets try that again!\n')


def new_event(start, end, name, email, details):
    """
    Makes an event entry in Google Calendar, getting data from
    the get_month function.

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

    CAL.events().insert(  # pylint: disable=maybe-no-member
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


welcome_screen()
