"""
Main file run.py, for FeelGood Physio by John Venkiah
This is the main file for a command line interface booking system for staff and
patients of fictive physiotherapist clinic FeelGood Physio.

The main objective is for users to book appointments and staff to check their
schedule, view and edit information.

The appointments are pushed to or read from a Google Calendar, and there is a
patient log saved as a Google sheet, stored on Google Drive.
"""

import datetime
import os
from datetime import timedelta
import re

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

import sheet
from cal_ops import CalOps
from time_f_converter import TimeFConverter
from inc_dec_week import IncDecWeek
if os.path.exists('password.py'):
    import password  # pylint: disable=unused-import  # noqa

# pylint: disable=pointless-string-statement
"""
Imports for all modules for application to function fully:

@datetime: For strings to be parsed as dates and time, and
for functions to return accurate time from Google Calendar API.
See https://docs.python.org/3/library/datetime.html for more details.

@os: Imported so that password can be stored locally in workspace
but also as config vars in Heroku. See
https://docs.python.org/3/library/os.html?highlight=os#module-os for details.

@datetime.timedelta: Used to add or subtract time from other time value.
Imported seperately so I don't have to use datetime.timedelta each time.

@build from googleapiclientdiscovery,
@Credentials from google.oauth2.service_account:
Needed for Google Calendar and Sheets API's to build resources
for the application to work.
See https://developers.google.com/calendar/api/v3/reference for details.

@re: For using regular expressions to validate user input. See
https://docs.python.org/3/library/re.html?highlight=re#module-re for details.
@sheet: The file in which functions for requests to Google Sheets API occur.

@password: When using from the terminal in IDE and not the deployed version,
imports password from local file instead.
"""

"""
SCOPES, CREDS, SCOPED_CREDS: used with Google API Client to gain access to
and modify data on Google Calendar and Google Sheets.
"""

SCOPES = 'http://www.googleapis.com/auth/calendar'

""" CREDS .json file created on Google Cloud Platform, stored as config vars
on Heroku.
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)

"""
CAL: The specific calendar on Google Calendar used in this project.
"""
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
    print('\nMade for patients and staff at the FeelGood Physio clinic\n')

    while True:
        staff_or_customer = input(
            'Press "b" to book an appointment or "s" for staff login:\n\n'
        )
        staff_or_customer = staff_or_customer.lower()

        if staff_or_customer == 's':
            staff_login()
            return False

        if staff_or_customer == 'b':
            suggest_appointment()
            return False

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


def staff_nav():
    """
    Displays the main staff menu for staff once password is entered correctly,
    with options to view patient log or schedule, or exit to the main screen.
    """

    while True:
        print('\nWhat would you like to view?\n')
        sche_or_log = input(
            'Schedule: "s", Patient Log: "l", Exit: any other key\n\n'
        )

        if sche_or_log == 's':
            print('\nChecking schedule...\n')

            d_1 = convert_time.iso_to_pretty(now, 0)
            d_2 = convert_time.iso_to_pretty(future_date(7), 0)

            print(f'Showing appointments between {d_1} and {d_2}\n')
            print_appointments(now, future_date(7))
            return False

        if sche_or_log == 'l':
            sheet.get_p_data()

            e_input = input(
                '\nPress e to exit or any other key for the staff menu.\n\n'
            )

            if e_input == 'e':
                e_to_exit(e_input)
                return False

        print('\nExiting...')
        welcome_screen()
        return False


def staff_login():
    """
    This is the staff area, from which staff members can access, change
    or delete patient data after successfully entering the password.
    """
    staff_password = os.environ['PASSWORD']
    attempts = 0
    staff_greeting = '\nFeelgood Physio - Staff login area\n'
    print(staff_greeting.upper())

    while True:
        password_entered = input(
            'Enter your password or "e" to exit:\n\n'
        )
        e_to_exit(password_entered)

        if attempts == 4:
            print('\nToo many incorrect attempts, exiting...\n')
            welcome_screen()
            return False

        if password_entered == staff_password:
            print('\nPassword correct!')
            staff_nav()
            return False

        print('\nWrong password, please try again\n')
        attempts += 1


def get_appointments(earliest, latest):
    """
    Get scheduled appointments for the given period from the Google Calendar

    @param earliest(str): starttime for period.
    @param latest(str): endtime for period.
    """

    appointments_result = CalOps.apt_list(CAL, CAL_ID, earliest, latest)

    appointments = appointments_result.get('items', [])
    return appointments


"""
An instance of the class used in nav_appntmnt function.
"""
week_multiplier = IncDecWeek()


def print_appointments(earliest, latest):
    """
    Print the appointments taken through the get_appointments function.

    """
    appointments = get_appointments(earliest, latest)
    app_nr = 1
    app_dict = {}

    if len(appointments) <= 3:
        print('Not many appointments that week.')

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
    nav_appntmnt(app_dict)


"""
Different instances of TimeFConverter, depending on needed format to display
or function as datetime on Google Calendar
"""
convert_time = TimeFConverter(
    '%Y-%m-%dT%H:%M:%S.%f' + GMT_OFF, '%H:%M, %d %b %Y'
)

convert_time_no_ms = TimeFConverter(
    '%Y-%m-%dT%H:%M:%S' + GMT_OFF, '%H:%M, %d %b %Y'
)

convert_time_staff = TimeFConverter(
    '%Y-%m-%dT%H:%M:%S' + GMT_OFF, '%H:%M, %d-%m-%Y'
)

convert_iso_iso_ms = TimeFConverter(
    '%Y-%m-%dT%H:%M:%S' + GMT_OFF, '%Y-%m-%dT%H:%M:%S.%f' + GMT_OFF
)


def nav_appntmnt(app_dict):
    """
    This lets staff navigate the schedule with week intervals,
    using week_nav_fn function to increment or decrement weeks. They can also
    edit or delete appointments.

    @param app_dict(dict): Dict keys are integers that are displayed next to
        each appointment for user to input, should they want to edit that
        specific appointment, and the Google Calendar event id as values.
    """
    print('\nTo edit an appointment, enter the appointment number.')
    print('\nTo get appointments for week after, press "n".')
    print('\nTo go back to the previous week, press "b".\n')
    nav_or_edit = input('Press any other key to get to the staff menu.\n\n')

    def week_nav_fn():
        """
        This lets staff navigate the schedule with week intervals,
        using week_nav_fn function to increment or decrement weeks.
        """

        days_1 = week_multiplier.get_value()
        days_2 = days_1 + 7
        date_1 = future_date(days_1)
        date_2 = future_date(days_2)
        d_pretty_1 = convert_time.iso_to_pretty(date_1, 0)
        d_pretty_2 = convert_time.iso_to_pretty(date_2, 0)
        print(
            f'\nAppointments between {d_pretty_1} and {d_pretty_2}:\n'
        )

        print_appointments(date_1, date_2)

    #  nav_appntmnt continues here
    if nav_or_edit == 'n':
        week_multiplier.increment()
        week_nav_fn()

    elif nav_or_edit == 'b':
        week_multiplier.decrement()
        week_nav_fn()

    elif str(nav_or_edit) in app_dict:
        apntmnt_id = app_dict[nav_or_edit]
        edit_appntmnt(nav_or_edit, apntmnt_id)

    else:
        print('\nExiting..')

        # pylint: disable=unused-variable
        days_1 = week_multiplier.initialize()  # noqa

        staff_nav()


def edit_appntmnt(nav_or_edit, apntmnt_id):
    """
    This lets staff navigate the schedule with week intervals,
    using week_nav_fn function to increment or decrement weeks.

    @param nav_or_edit(str): Input from user.
    @param apntmnt_id(int): Value stored in apntmnt_dict to pinpoint
        specific event on Google Calendar.
    """
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
            # pylint: disable=maybe-no-member
            CalOps.del_apt(CAL, CAL_ID, apntmnt_id)
            # CAL.events().delete(  
            #     calendarId=CAL_ID,
            #     eventId=apntmnt_id
            # ).execute()

            print('\nAppointment deleted!\n')
            print_appointments(now, future_date(7))
        else:
            print('\n\nCancelled.\n')
            edit_appntmnt(nav_or_edit, apntmnt_id)

    elif edit_or_delete == 'e':
        # pylint: disable=maybe-no-member
        apntmnt_to_edit = CalOps.get_apt(CAL, CAL_ID, apntmnt_id)
        # apntmnt_to_edit = CAL.events().get(
        #     calendarId=CAL_ID,
        #     eventId=apntmnt_id
        # ).execute()

        edit_appntmnt_2(apntmnt_to_edit, apntmnt_id)

    else:
        print('Cancelled.')
        print_appointments(now, future_date(7))


def edit_appntmnt_2(apntmnt_to_edit, apntmnt_id):
    """
    Lets user choose what to edit for the chosen appointment.

    @param apntmnt_to_edit: The specific event to edit.
    @param apntmnt_id(int): Value stored in apntmnt_dict to pinpoint
        specific event on Google Calendar.
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
        print_appointments(now, future_date(7))
        return


def get_name_staff(apntmnt_to_edit, apntmnt_id):
    """
    Lets user edit patient name.

    @param apntmnt_to_edit: The specific event to edit.
    @param apntmnt_id(int): Value stored in apntmnt_dict to pinpoint
        specific event on Google Calendar.
    """

    print('\nPlease enter new name:\n')
    new_name = validate_name()
    update_name(apntmnt_to_edit, apntmnt_id, new_name)


def get_date_staff(apntmnt_to_edit, apntmnt_id):
    """
    Lets user enter appointment date, slightly simpler that the patient
    version.

    @param apntmnt_to_edit: The specific event to edit.
    @param apntmnt_id(int): Value stored in apntmnt_dict to pinpoint
        specific event on Google Calendar.
    """

    while True:

        print('\nEnter new date for appointment, in this format:\n')
        date_input = input("DD-MM-YY (don't forget the hyphens)\n\n")

        try:
            date_input = datetime.datetime.strptime(date_input, '%d-%m-%y')
            date_input = date_input.date()
            date_input = date_input.strftime('%d-%m-%Y')
            add_time_staff(date_input, apntmnt_to_edit, apntmnt_id)
            return False

        except ValueError as error:
            print(f'\nInvalid date: {error}, please try again.')


def get_details_staff(apntmnt_to_edit, apntmnt_id):
    """
    Lets user edit email and notes for patients, showing current data first.

    @param apntmnt_to_edit: The specific event to edit.
    @param apntmnt_id(int): Value stored in apntmnt_dict to pinpoint
        specific event on Google Calendar.
    """
    name = apntmnt_to_edit['summary']
    print(f'\nDetails for {name}:')

    if 'description' in apntmnt_to_edit:
        print('\n' + apntmnt_to_edit['description'])

    else:
        print(f'\nNo details for {name}')

    new_details = input('\nEnter new patient details here:\n\n')

    print(f'\nAccept update "{new_details}" for {name}?\n')
    update_details = input('("y" for YES, any other key for NO)\n\n')

    if update_details.lower() == 'y':

        apntmnt_to_edit['description'] = new_details
        update_cal(apntmnt_id, apntmnt_to_edit)

        print(f'\nDetails for {name} updated.')

        print_appointments(now, future_date(7))
        return

    print('Cancelled, getting main menu...')
    staff_nav()


def update_name(apntmnt_to_edit, apntmnt_id, new_name):
    """
    Updates Google Calendar event ['summary'] which displays the patient name.

    @param apntmnt_to_edit: The specific event to edit.
    @param apntmnt_id(int): Value stored in apntmnt_dict to pinpoint
        specific event on Google Calendar.
    @param new_name(str): The name input from user to update event with.
    """

    apntmnt_to_edit['summary'] = new_name

    update_cal(apntmnt_id, apntmnt_to_edit)

    print(f'\nAppointment name updated: {new_name}\n')
    print_appointments(now, future_date(7))


def add_time_staff(date_input, apntmnt_to_edit, apntmnt_id):
    """
    Allows staff to enter new time for appointment.

    @param month(str): Month given by user
    @param year(str): Year given by user
    """
    while True:

        print(f'\n{date_input}. What time? Enter hour, two digits.\n')
        get_hour = input('Enter hour, 9 - 17 ("e" to exit):\n\n')

        if get_hour.lower() == 'e':
            staff_nav()
            return False

        if get_hour.isnumeric() and int(get_hour) >= 9 and int(get_hour) < 17:

            get_hour = get_hour + ':00'
            apntmnt_time = (f'{get_hour}, {date_input}')
            apntmnt_time = convert_time_staff.pretty_to_iso(apntmnt_time, 0)
            end_time = convert_iso_iso_ms.add_hour_iso(apntmnt_time, +1)

            appointments = get_appointments(apntmnt_time, end_time)

            if appointments:
                print('\nSorry, appointment not available. Try again.')
            else:
                print(f'\n{get_hour} on {date_input} is free.\n')

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

                print('\nCancelled. Getting the coming week:')
                print_appointments(now, future_date(7))
        else:
            print('\nSorry, invalid entry.')


def update_apntmnt_time(apntmnt_time, end_time, apntmnt_to_edit, apntmnt_id):
    """
    Passes start and end time to update_cal function to update event with.

    @param apntmnt_time(str): Start time for event
    @param end_time(str): End time for event
    @param apntmnt_to_edit: Instance of CAL-resource updating calendar
    @param apntmnt_id(str): Google Calendar event identifier
    """

    apntmnt_to_edit['start']['dateTime'] = apntmnt_time
    apntmnt_to_edit['end']['dateTime'] = end_time

    update_cal(apntmnt_id, apntmnt_to_edit)

    apntmnt_time = convert_time_no_ms.iso_to_pretty(apntmnt_time, 0)

    print('\nAppointment time updated:\n')
    print(apntmnt_time + ', ' + apntmnt_to_edit['summary'] + '\n')

    go_back = input('Press any key to see current schedule for the week.\n\n')

    if go_back != '¶¥¿':
        print_appointments(now, future_date(7))


def update_cal(apntmnt_id, apntmnt_to_edit):
    """
    Update the Google Calendar event with the input from the previous
    functions from user.

    @param apntmnt_id(str): Google Calendar event identifier
    @param apntmnt_to_edit: Instance of CAL-resource updating calendar
    """
    # pylint: disable=maybe-no-member
    CalOps.updt_apt(CAL, CAL_ID, apntmnt_id, apntmnt_to_edit)
    # CAL.events().update(
    #     calendarId=CAL_ID,
    #     eventId=apntmnt_id,
    #     body=apntmnt_to_edit
    # ).execute()


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

    days = 29 if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0) else 28
    return days


def get_month(yr):  # pylint: disable=invalid-name
    """
    Initiate the booking process and gets month from user for appointment.

    @param yr(int): the year of the appointment.
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
                yr = datetime.datetime.today() + timedelta(365.2425)
                yr = yr.yr

            get_date(days_in_month, month, yr, int_month, int_this_month)
            return False

        if month.isnumeric():
            print(month_incorr)

        else:
            print(month_incorr)


def get_date(
    days_in_month, month, yr, int_month, int_this_month
):  # pylint: disable=invalid-name

    """
    Get the date from the user, with the month and year
    passed from the above function

    @param days_in_month(str): Number representing days in given month
        from month_dict.
    @param month(str): Month given by user
    @param yr(str): Year given by user
    @param int_month(int): A number for month, eg 12 for Dec
    """

    while True:

        print(f'\n{month}, {yr}. Which date?\n')
        date = input('Enter two digits, ("e" to exit):\n\n')
        date_incorrect = '\nDate incorrect, please try again'
        e_to_exit(date)

        try:
            date_today = datetime.date.today().day
            weekday_int = datetime.date(
                yr, int_this_month, int(date)
            ).weekday()

            if (
                int_month == int_this_month and int(date) <= date_today or
                weekday_int == 5 or weekday_int == 6
            ):
                print(
                    '\nBooking has to be at least one day ahead, no weekends.'
                )

            elif int(date) <= int(days_in_month) and int(date) > 0:
                get_time(date, month, yr)
                return False

        except ValueError:
            print(date_incorrect)


def get_time(date, month, yr):  # pylint: disable=invalid-name
    """
    Get the date from the user, with the month and year
    passed from the above function

    @param date(str): Date given by user
    @param month(str): Month given by user
    @param yr(str): Year given by user
    """
    while True:

        print(f'\n{date} {month}, {yr}. What time?\n')
        hour = input('Enter hour, 9 - 17 ("e" to exit):\n\n')

        e_to_exit(hour)

        if hour.isnumeric() and int(hour) >= 9 and int(hour) < 17:
            apntmnt_time = (f'{hour}:00, {date} {month} {yr}')

            apntmnt_time = convert_time.pretty_to_iso(apntmnt_time, 0)
            end_time = convert_time.add_hour_iso(apntmnt_time, +1)

            appointments = get_appointments(apntmnt_time, end_time)

            if appointments:
                print('Sorry, appointment not available. Try again.')
            else:
                print(f'{hour}:00 on {date} {month}, {yr} is free.\n')
                get_name(apntmnt_time, end_time)
                return False
        else:
            print('\nSorry, invalid entry.')


def validate_name():
    """
    Simple name validation so user inputs two names and without numbers.
    """

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

    @param apntmnt_time(str): Start time of appointment
    @param end_time(str): Start time of appointment
    """

    print('To continue, enter your full name ("e" to exit):\n')
    name = validate_name()
    print(f'\nThank you {name}.\n')
    get_email(apntmnt_time, end_time, name)
    return name


def get_email(apntmnt_time, end_time, name):
    """
    Get email from the user, and validate it with simple regular expression.

    @param apntmnt_time(str): Start time of appointment
    @param end_time(str): End time of appointment
    @param name(str): Name to display as ['summary'] for Google event
    """
    while True:
        email = input('Please enter your email ("e" to exit):\n\n')
        e_to_exit(email)

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            print('\nInvalid email, try again\n')

        else:
            get_details(apntmnt_time, end_time, name, email)
            return False


def get_details(apntmnt_time, end_time, name, email):
    """
    Lets user describe symptoms and saves info as details
    variable in description.

    @param apntmnt_time(str): Start time of appointment
    @param end_time(str): End time of appointment
    @param name(str): Name to display as ['summary'] for Google event
    """
    while True:
        details = input('\nShortly describe your symptoms ("e" to exit):\n\n')
        e_to_exit(details)

        if len(details) < 8:
            print('\nPlease enter at least eight characters')

        else:
            start_pretty = convert_time.iso_to_pretty(apntmnt_time, 0)

            print(f'\nConfirm appointment: {start_pretty}?\n')
            confirm = input('"y" = YES, any other key = NO\n\n')

            if confirm.lower() == 'y':
                new_appointment(
                    apntmnt_time, end_time, name, email,
                    details, start_pretty
                )
                return False

            print('\nAppointment Cancelled!')


def new_appointment(
    start, end, name, email, details, start_pretty
):  # pylint: disable=too-many-arguments

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
        event = {
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
            sendNotifications=True, body=event).execute()

        print(f'\nThanks, {name}, appointment added:\n')
        print(f'{start_pretty}, {email}\n')
        print(details)
        print('\nLogging your details...')
        sheet.append_p_row(name, email, details)

        goback = input('\nPress any key to go back to the start screen.\n\n')
        if goback != '¶':
            welcome_screen()

    except Exception as error:  # pylint: disable=broad-except
        print('Could not add appointment, possible Google API Error:' + error)
        welcome_screen()


welcome_screen()
