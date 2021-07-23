from __future__ import print_function
import stdiomask
import password
import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import re
import sheet

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
    print('Your data will be saved to our database upon confirmation.\n')
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


def staff_nav():
    while True:
        print('\nWhat would you like to view?\n')
        sche_or_log = input(
            'Schedule: "s", Patient Log: "l", Exit: any other key\n\n'
        )

        if sche_or_log == 's':
            get_appointments(now, future_date(7))
            d_1 = convert_time.iso_to_pretty(now, 0)
            d_2 = convert_time.iso_to_pretty(future_date(7), 0)
            print(f'Showing appointments between {d_1} and {d_2}\n')
            print_appointments()
            return False

        elif sche_or_log == 'l':
            sheet.get_p_data(sheet.p_log)

            e = input(
                '\nPress e to exit or any other key for the staff menu.\n\n'
            )

            if e == 'e':
                e_to_exit(e)
                return False

        else:
            print('\nExiting...')
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
            print('\nPassword correct!')
            staff_nav()
            return False

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

    appointments_result = CAL.events().list(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        timeMin=earliest,
        timeMax=latest,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    global appointments
    appointments = appointments_result.get('items', [])
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


week_multiplier = Inc_dec_week()


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

        start = convert_time_no_ms.iso_to_pretty(start, 0)

        event_id = appointment['id']

        app_dict.update({f'{app_nr}': event_id})

        if 'description' not in appointment:
            appointment.update({'description': 'No info'})

        if 'summary' not in appointment:
            appointment.update({'summary': 'No name'})
        print(
            f'{app_nr}: ', start, appointment['summary'],
            appointment['description']
            )
        app_nr += 1
    nav_appntmnt(week_multiplier, app_dict)


class Time_F_Converter():

    def __init__(self, str_iso, str_pretty):
        self.str_iso = str_iso
        self.str_pretty = str_pretty

    def iso_to_pretty(self, date, offset):
        date = datetime.datetime.strptime(date, self.str_iso)
        date = date + timedelta(hours=offset)
        return date.strftime(self.str_pretty)

    def pretty_to_iso(self, date, offset):
        date = datetime.datetime.strptime(date, self.str_pretty)
        date = date + timedelta(hours=offset)
        return date.strftime(self.str_iso)

    def add_hour_iso(self, date, offset):
        date = datetime.datetime.strptime(date, self.str_iso)
        date = date + timedelta(hours=offset)
        return date.strftime(self.str_iso)


convert_time = Time_F_Converter(
    '%Y-%m-%dT%H:%M:%S.%f' + GMT_OFF, '%H:%M, %d %b %Y'
)

convert_time_no_ms = Time_F_Converter(
    '%Y-%m-%dT%H:%M:%S' + GMT_OFF, '%H:%M, %d %b %Y'
)

convert_time_staff = Time_F_Converter(
    '%Y-%m-%dT%H:%M:%S' + GMT_OFF, '%H:%M, %d-%m-%Y'
)

convert_iso_iso_ms = Time_F_Converter(
    '%Y-%m-%dT%H:%M:%S' + GMT_OFF, '%Y-%m-%dT%H:%M:%S.%f' + GMT_OFF
)


def nav_appntmnt(week_multiplier, app_dict):
    print('\nTo edit an appointment, enter the appointment number.')
    print('\nTo get appointments for week after, press "n".')
    print('\nTo go back to the previous week, press "b".\n')
    nav_or_edit = input('Press any other key to get to the staff menu.\n\n')

    def week_nav_fn(week_multiplier):
        days_1 = week_multiplier.get_value()
        days_2 = days_1 + 7
        date_1 = future_date(days_1)
        date_2 = future_date(days_2)
        d_pretty_1 = convert_time.iso_to_pretty(date_1, 0)
        d_pretty_2 = convert_time.iso_to_pretty(date_2, 0)
        print(
            f'\nAppointments between {d_pretty_1} and {d_pretty_2}:'
        )

        get_appointments(date_1, date_2)
        print_appointments()

    if nav_or_edit == 'n':
        week_multiplier.increment()
        week_nav_fn(week_multiplier)

    elif nav_or_edit == 'b':
        week_multiplier.decrement()
        week_nav_fn(week_multiplier)

    elif str(nav_or_edit) in app_dict:
        apntmnt_id = app_dict[nav_or_edit]
        edit_appntmnt(nav_or_edit, apntmnt_id)
        return

    else:
        print('\nExiting..')
        staff_nav()
        return


def edit_appntmnt(nav_or_edit, apntmnt_id):
    print(f'\nAppointment {nav_or_edit}:\n')
    edit_or_delete = input(
        'Press "e" to edit, "r" to remove or any other key to go back.\n\n'
    )

    if edit_or_delete == 'r':

        sure = input(
            '\nDelete appointment ' + nav_or_edit +
            ' ("y": YES, any other key: NO)?\n\n'
        )

        if sure == 'y':

            CAL.events().delete(  # pylint: disable=maybe-no-member
                calendarId=CAL_ID,
                eventId=apntmnt_id
            ).execute()

            print('\nAppointment deleted!')
            get_appointments(now, future_date(7))
            print_appointments()
        else:
            print('\nCancelled.')
            edit_appntmnt(nav_or_edit, apntmnt_id)

    elif edit_or_delete == 'e':

        apntmnt_to_edit = CAL.events().get(  # pylint: disable=maybe-no-member
            calendarId=CAL_ID,
            eventId=apntmnt_id
        ).execute()

        edit_appntmnt_2(apntmnt_to_edit, apntmnt_id)

    else:
        print('Cancelled.')
        get_appointments(now, future_date(7))
        print_appointments()


def edit_appntmnt_2(apntmnt_to_edit, apntmnt_id):
    """
    Edit the start and end time of the appointment.

    @param apntmnt_to_edit (int): The specific event passed to change.
    """

    print('\nEdit appointment - choose what to edit:')
    print('\nTime: "t"                | Name: "n"\n')
    change_choice = input(
        'Details / Email: "d"   | Exit: any other\n\n'
    )

    if change_choice.lower() == 't':
        get_date_staff(apntmnt_to_edit, apntmnt_id)

    elif change_choice.lower() == 'n':
        get_name_staff(apntmnt_to_edit, apntmnt_id)

    elif change_choice.lower() == 'd':
        get_details_staff(apntmnt_to_edit, apntmnt_id)

    else:
        get_appointments(now, future_date(7))
        print_appointments()
        return


def get_name_staff(apntmnt_to_edit, apntmnt_id):

    print('\nPlease enter new name:\n')
    new_name = validate_name()
    update_name(apntmnt_to_edit, apntmnt_id, new_name)


def get_date_staff(apntmnt_to_edit, apntmnt_id):

    while True:

        print('\nEnter new date for appointment, in this format:\n')
        date_input = input("DD-MM-YY (don't forget the hyphens)\n\n")

        try:
            date_input = datetime.datetime.strptime(date_input, '%d-%m-%y')
            date_input = date_input.date()
            date_input = date_input.strftime('%d-%m-%Y')
            add_time_staff(date_input, apntmnt_to_edit, apntmnt_id)
            return False

        except ValueError as e:
            print(f'\nInvalid date: {e}, please try again.')


def get_details_staff(apntmnt_to_edit, apntmnt_id):
    name = apntmnt_to_edit['summary']
    print(f'\nDetails for {name}:')

    if 'description' in apntmnt_to_edit:
        print('\n' + apntmnt_to_edit['description'])

    else:
        print(f'\nNo details for {name}')

    new_details = input('\nEnter new patient details here:\n\n')

    print(f'\nAccept update "{new_details}" for {name}?\n')
    update_details = input('("y" for YES, "n" for NO)\n\n')

    if update_details.lower() == 'y':

        apntmnt_to_edit['description'] = new_details
        update_cal(apntmnt_id, apntmnt_to_edit)

        print(f'\nDetails for {name} updated.')

        get_appointments(now, future_date(7))
        print_appointments()
        return

    else:
        print('invalid entry, please try again.')


def update_name(apntmnt_to_edit, apntmnt_id, new_name):
    apntmnt_to_edit['summary'] = new_name

    update_cal(apntmnt_id, apntmnt_to_edit)

    print(f'\nAppointment name updated: {new_name}')
    get_appointments(now, future_date(7))
    print_appointments()


def add_time_staff(date_input, apntmnt_to_edit, apntmnt_id):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param month(str): Month given by user
    @param year(str): Year given by user
    """
    while True:

        print(f'\n{date_input}. What time? Enter hour, two digits.\n')
        get_hour = input('Enter hour, 9 - 17 ("e" to exit):\n\n')

        e_to_exit(get_hour)

        if get_hour.isnumeric() and int(get_hour) >= 9 and int(get_hour) < 17:

            get_hour = get_hour + ':00'
            apntmnt_time = (f'{get_hour}, {date_input}')
            apntmnt_time = convert_time_staff.pretty_to_iso(apntmnt_time, 0)
            end_time = convert_iso_iso_ms.add_hour_iso(apntmnt_time, +1)

            get_appointments(apntmnt_time, end_time)

            if appointments:
                print('Sorry, appointment not available. Try again.')
            else:
                print(f'{get_hour} on {date_input} is free.\n')

                if 'summary' not in apntmnt_to_edit:
                    apntmnt_to_edit.update({'summary': 'No info'})
                    print(
                        'confirm ' + get_hour + ' , ' + date_input + ' for ' +
                        apntmnt_to_edit['summary'] + '?\n'
                    )

                conf_new_time = input(
                    '"y" for yes, any other key for "no"\n\n'
                )

                if conf_new_time == 'y':
                    update_apntmnt_time(
                        apntmnt_time, end_time, apntmnt_to_edit, apntmnt_id
                    )
                    return False

                else:
                    print('\nCancelled. Getting the coming week:')
                    get_appointments(now, future_date(7))
                    print_appointments()
        else:
            print('\nSorry, invalid entry.')


def update_apntmnt_time(apntmnt_time, end_time, apntmnt_to_edit, apntmnt_id):

    apntmnt_to_edit['start']['dateTime'] = apntmnt_time
    apntmnt_to_edit['end']['dateTime'] = end_time

    update_cal(apntmnt_id, apntmnt_to_edit)

    apntmnt_time = convert_time_no_ms.iso_to_pretty(apntmnt_time, 0)

    print('\nAppointment time updated:\n')
    print(apntmnt_time + ', ' + apntmnt_to_edit['summary'] + '\n')

    go_back = input('Press any key to see current schedule for the week.\n\n')

    if go_back != '¶¥¿':
        get_appointments(now, future_date(7))
        print_appointments()


def update_cal(apntmnt_id, apntmnt_to_edit):
    CAL.events().update(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        eventId=apntmnt_id,
        body=apntmnt_to_edit
    ).execute()


def future_date(day):
    """
    Gives a day in the future in datetime format depending on day parameter.

    @param day (int): Amount of days from now into the future to return.
    """

    date = datetime.datetime.now() + timedelta(day)
    date = date.isoformat() + GMT_OFF
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
        month_incorr = '\nMonth incorrect, please try again'

        e_to_exit(month)

        if month in month_dict.keys():
            int_month = datetime.datetime.strptime(month, '%b')
            int_month = int(int_month.strftime('%m'))

            this_month = datetime.datetime.now().month
            int_this_month = int(this_month)

            if int_month < int_this_month:
                year = datetime.datetime.today() + timedelta(365.2425)
                year = year.year

            get_date(days_in_month, month, year, int_month, int_this_month)
            return False

        elif month.isnumeric():
            print(month_incorr)

        else:
            print(month_incorr)


def get_date(days_in_month, month, year, int_month, int_this_month):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param month(str): Month given by user
    @param year(str): Year given by user
    """

    while True:

        print(f'\n{month}, {year}. Which date?\n')
        date = input('Enter two digits, ("e" to exit):\n\n')
        date_incorrect = '\nDate incorrect, please try again'

        try:
            date_today = datetime.date.today().day
            weekday_int = datetime.date(
                year, int_this_month, int(date)
            ).weekday()
            e_to_exit(date)

            if (
                int_month == int_this_month and int(date) <= date_today
                or weekday_int == 5 or weekday_int == 6
            ):
                print(
                    '\nBooking has to be at least one day ahead, no weekends.'
                )

            elif int(date) <= int(days_in_month) and int(date) > 0:
                get_time(date, month, year)
                return False

        except ValueError:
            print(date_incorrect)


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

            apntmnt_time = convert_time.pretty_to_iso(apntmnt_time, 0)
            end_time = convert_time.add_hour_iso(apntmnt_time, +1)

            get_appointments(apntmnt_time, end_time)

            if appointments:
                print('Sorry, appointment not available. Try again.')
            else:
                print(f'{hour}:00 on {date} {month}, {year} is free.\n')
                get_name(apntmnt_time, end_time)
                return False
        else:
            print('\nSorry, invalid entry.')


def validate_name():

    while True:
        name = input()
        e_to_exit(name)
        if any(char.isdigit() for char in name):
            print("\nName can't contain numbers!\n")

        elif name.__contains__(' '):
            return name

        else:
            print("\nFirst and last name please.\n")


def get_name(apntmnt_time, end_time):
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param start(str): Start time of appointment
    @param end(str): Start time of appointment
    """

    print('To continue, enter your full name ("e" to exit):\n')
    name = validate_name()
    print(f'\nThank you {name}.\n')
    get_email(apntmnt_time, end_time, name)
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

        if len(details) < 8:
            print('\nPlease enter at least eight characters')

        else:
            start_time_pretty = convert_time.iso_to_pretty(apntmnt_time, 0)

            print(f'\nConfirm appointment: {start_time_pretty}?\n')
            confirm = input('"y" = YES, any other key = NO\n\n')

            if confirm.lower() == 'y':
                new_appointment(
                    apntmnt_time, end_time, name, email,
                    details, start_time_pretty
                )
                return False

            else:
                print('\nAppointment Cancelled!')


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
    try:
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

        CAL.events().insert(  # pylint: disable=maybe-no-member
            calendarId=CAL_ID,
            sendNotifications=True, body=APPOINTMENT).execute()

        print(f'\nThanks, {name}, appointment added:\n')
        print(f'{start_time_pretty}, {email}\n')
        print(details)
        print('Logging your details...')
        sheet.append_p_row(name, email, details)

        goback = input('\nPress any key to go back to the start screen.\n\n')
        if goback != '¶':
            welcome_screen()

    except Exception as e:
        print(f'\nCould not add appointment, possible Google API Error: {e}')
        welcome_screen()

welcome_screen()
