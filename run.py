from __future__ import print_function
import stdiomask
import password
import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import re

SCOPES = 'http://www.googleapis.com/auth/calendar'
CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
CAL = build('calendar', 'v3', credentials=CREDS)
CAL_ID = 'uueq3s2tbgdl57dvmmvcp5osd8@group.calendar.google.com'
GMT_OFF = '+01:00'
year = datetime.date.today().year
now = datetime.datetime.utcnow().isoformat() + GMT_OFF


def welcome_screen():
    """
    The patient or staff member is greeted with this welcome screen,
    from here users can either choose the patient or staff section.
    """
    welcome_greeting = '\nWelcome to the Feelgood Physio booking system\n'
    print(welcome_greeting.upper())

    while True:

        staff_or_customer = input(
            'Press "b" to book an appointment or "s" for staff login:\n\n'
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

    print("\nLet's find you an appointment.\n")
    book_or_back = input(
        'Press "1" to continue or any other key to go back.\n\n'
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
    staff_greeting = '\nFeelgood Physio - Staff login area\n'
    print(staff_greeting.upper())

    while True:

        password_entered = stdiomask.getpass(
            'Enter your password or "e" to exit:\n\n'
        )

        e_to_exit(password_entered)

        if attempts == 4:
            print('\nToo many incorrect attempts, exiting...\n')
            welcome_screen()
            return False

        if password_entered == password.password:
            print(
                '\nPassword correct, getting schedule for coming week:'
            )
            get_appointments(now, future_date(7))
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

    print('\nChecking schedule...')
    global now
    now = datetime.datetime.now().isoformat()
    now = now + 'Z'

    appointments_result = CAL.events().list(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        timeMin=earliest,
        timeMax=latest,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    global appointments
    appointments = appointments_result.get('items', [])

    print(f'\nAppointments between {earliest} and {latest}:\n')
    return appointments


class Inc_dec_week():
    def __init__(self):
        self.inc_dec_week = 0

    def increment(self):
        self.inc_dec_week += 7

    def decrement(self):
        self.inc_dec_week -= 7

    def get_value(self):
        return self.inc_dec_week


weeks_multiplier = Inc_dec_week()


def print_appointments():
    """
    Print the appointments taken through the get_appointments function.

    """
    app_nr = 1
    app_dict = {}

    if not appointments or len(appointments) <= 2:
        print('No appointments that week.')

    for appointment in appointments:

        start = appointment['start'].get('dateTime')
        if start is None:
            continue
        start = datetime.datetime.strptime(
            start, '%Y-%m-%dT%H:%M:%S' + GMT_OFF
        )
        start = start.strftime("%H:%M, %d %b %Y")

        event_id = appointment['id']

        app_dict.update({f'{app_nr}': event_id})

        if 'description' not in appointment:
            appointment.update({'description': 'No info'})
        print(
            f'{app_nr}: ', start, appointment['summary'],
            appointment['description'], f'{app_dict}'
            )
        app_nr += 1
    nav_appntmnt(weeks_multiplier, app_dict)


def nav_appntmnt(weeks_multiplier, app_dict):
    print('\nTo edit an appointment, enter the appointment number.')
    print('\nTo get appointments for week after, press "n".')
    print('\nTo go back to the previous week, press "b".\n')
    nav_or_edit = input('Press "e" to exit:\n\n')

    if nav_or_edit == 'n':
        weeks_multiplier.increment()
        days_1 = weeks_multiplier.get_value()
        days_2 = days_1 + 7
        get_appointments(future_date(days_1), future_date(days_2))
        print_appointments()

    elif nav_or_edit == 'b':
        weeks_multiplier.decrement()
        days_1 = weeks_multiplier.get_value()
        days_2 = days_1 + 7
        get_appointments(future_date(days_1), future_date(days_2))
        print_appointments()
    
    elif str(nav_or_edit) in app_dict:
        apntmnt_id = app_dict[nav_or_edit]
        edit_appntmnt(nav_or_edit, apntmnt_id)
        return

    else:
        print(type(nav_or_edit))
        print(f'\n{nav_or_edit} Exiting..')
        welcome_screen()
        return


def edit_appntmnt(nav_or_edit, apntmnt_id):
    print(f'\nAppointment {nav_or_edit}:')
    delete_or_not = input(
        'Press "c" to change, "d" to remove or any other key to go back.\n'
    )

    if delete_or_not == 'd':

        sure = input(f'Delete appointment {nav_or_edit}?\n')

        if sure == 'd':
    
            CAL.events().delete(
                calendarId=CAL_ID, eventId=apntmnt_id
            ).execute()

            print('Appointment deleted!\n')
        
        else:
            print('Cancelled.')
            edit_appntmnt(nav_or_edit, apntmnt_id)

    elif delete_or_not == 'c':

        apntmnt_to_edit = CAL.events().get(
            calendarId=CAL_ID, eventId=apntmnt_id
        ).execute()
        change_appntmnt(apntmnt_to_edit, apntmnt_id)


    else:
        print('Cancelled.')
        get_appointments(now, future_date(7))
        print_appointments()


def change_appntmnt(apntmnt_to_edit, apntmnt_id):
    """
    Edit the start and end time of the appointment.

    @param apntmnt_to_edit (int): The specific event passed to change.
    """
    change = input('Change event?')
    if change == 'y':

        get_start_time = apntmnt_to_edit['start'].get('dateTime')
        get_end_time = apntmnt_to_edit['end'].get('dateTime')

        get_start_time = datetime.datetime.strptime(
            get_start_time, '%Y-%m-%dT%H:%M:%S' + GMT_OFF
        )

        get_end_time = datetime.datetime.strptime(
            get_end_time, '%Y-%m-%dT%H:%M:%S' + GMT_OFF
        )
        """

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

        """

        new_start_time = get_start_time + timedelta(hours=+1)
        new_end_time = get_end_time + timedelta(hours=+1)

        new_start_time = new_start_time.strftime('%Y-%m-%dT%H:%M:%S' + GMT_OFF)
        new_end_time = new_end_time.strftime('%Y-%m-%dT%H:%M:%S' + GMT_OFF)

        apntmnt_to_edit['start']['dateTime'] = new_start_time
        apntmnt_to_edit['end']['dateTime'] = new_end_time

        updated_apntmnt = CAL.events().update(
            calendarId=CAL_ID, eventId=apntmnt_id, body=apntmnt_to_edit
        ).execute()

        print(updated_apntmnt['updated'])

    return


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

        print('\nChoose the month for the appointment.\n')
        month = input('3 letters, first capital. "e" to exit.\n\n')
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
            print('\nMonth incorrect, please try again\n')
        else:
            print('\nMonth incorrect, please try again\n')


def get_date(days_in_month, month, year):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param month(str): Month given by user
    @param year(str): Year given by user
    """

    while True:

        print(f'\n{month}, {year}. Which date?\n')
        date = input('Enter two digits, ("e" to exit):\n\n')

        e_to_exit(date)

        if (
            date.isnumeric() and
            int(date) <= int(days_in_month) and
            int(date) > 0
        ):
            get_time(date, month, year)
            return False
        else:
            print('\nDate incorrect, please try again')


def get_time(date, month, year):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param month(str): Month given by user
    @param year(str): Year given by user
    """
    while True:

        print(f'\n{date} {month}, {year}. What time?\n')
        hour = input('Enter hour, 9 - 17 ("e" to exit):\n\n')

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

            if appointments:
                print('Sorry, appointment not available. Try again.')
            else:
                print(f'{hour}:00 on {date} {month}, {year} is free.\n')
                get_name(apntmnt_time, end_time)
                return False
        else:
            print('\nSorry, invalid entry.')


patient_dict = {
                'name': '',
                'email': '',
                'appointment': '',
                'symtoms': '',
                }


def get_name(apntmnt_time, end_time):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param start(str): Start time of appointment
    @param end(str): Start time of appointment
    """

    while True:

        name = input('To continue, enter your full name ("e" to exit):\n\n')
        e_to_exit(name)

        if any(char.isdigit() for char in name):
            print("\nName can't contain numbers!\n")
            continue

        elif name.__contains__(' '):
            print(f'\nThank you, {name}.\n')
            get_email(apntmnt_time, end_time, name)
            return False

        else:
            print("\nFirst and last name please\n")

    return name


def get_email(apntmnt_time, end_time, name):

    while True:

        email = input('Please enter your email ("e" to exit):\n\n')
        e_to_exit(email)

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            print('\nInvalid email, try again\n')
        else:
            get_details(apntmnt_time, end_time, name, email)

    return False


def get_details(apntmnt_time, end_time, name, email):

    while True:
        details = input('\nShortly describe your symptoms ("e" to exit):\n\n')
        e_to_exit(details)

        start_time_pretty = datetime.datetime.strptime(
            apntmnt_time, '%Y-%m-%dT%H:%M:%S' + GMT_OFF
        )

        start_time_pretty = start_time_pretty.strftime('%H:%M, %d %b %Y')

        print(f'\nConfirm appointment: {start_time_pretty}?\n')
        confirm = input('"y" = YES, any other key = NO\n\n')

        if confirm.lower() == 'y':
            new_appointment(
                apntmnt_time, end_time, name, email, details, start_time_pretty
            )
            return False

        else:
            print('\nAppointment Cancelled!\n')


def new_appointment(start, end, name, email, details, start_time_pretty):
    """
    Makes an appointment entry in Google Calendar, getting data from
    the get_month function.

    @param start(str): Start time of appointment
    @param end(str): Start time of appointment
    @param name(str): Name entered by patient
    @param email(str): Email entered by patient
    @param details(str): Description of symptoms entered by patient
    """

    APPOINTMENT = {
        'start': {
            'dateTime': start,
            },
        'end': {
            'dateTime': end,
            },
        'summary': name,
        'description': f'{email}, {details}'
    }

    CAL.appointments().insert(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        sendNotifications=True, body=APPOINTMENT).execute()

    print(f'\nThanks, {name}, appointment added:\n')
    print(f'{start_time_pretty}, {email}\n')
    print(details)
    goback = input('\nPress any key to go back to the beginning\n\n')

    if goback != '¶':
        welcome_screen()


welcome_screen()
