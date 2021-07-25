"""
cal_mod, Calendar operations module for Feegood Physio Application
Contains functions to call Google API Calendar and get or recieve data to be
passed to the functions in run.py.
"""


def apt_list(cal, c_id, start, end):
    """
    Gets a list of event dictionaries from the Calendar.

    @param cal(resource): The calendar being called
    @param c_id(str): The calendar ID
    @param start(str): The start time of the period or events
    @param end(str): The end time of the period or events
    """

    appointments_result = cal.events().list(
        calendarId=c_id,
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    appointments = appointments_result.get('items', [])
    return appointments
    # return appointments_result


def del_apt(cal, c_id, apt_id):
    """
    Deletes a specific event from the Google calendar chosen by user.

    @param cal(resource): The calendar being called
    @param c_id(str): The calendar ID
    @param apt_id(str): The Google event ID of the specific event to be deleted
    """

    cal.events().delete(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        eventId=apt_id
    ).execute()


def get_apt(cal, c_id, apt_id):
    """
    Gets a specific event from the Google Calendar.

    @param cal(resource): The calendar being called
    @param c_id(str): The calendar ID
    @param apt_id(str): The Google event ID of the specific event to be
        retreived
    """

    apntmnt_to_edit = cal.events().get(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        eventId=apt_id
    ).execute()
    return apntmnt_to_edit


def updt_apt(cal, c_id, apt_id, apmnt):
    """
    Update the Google Calendar event with the input from the previous
    functions from user.

    @param apt_id(str): Google Calendar event identifier
    @param apmnt(dict): The appointment passed to the calendar
    """
    cal.events().update(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        eventId=apt_id,
        body=apmnt
    ).execute()


def insrt_apt(cal, c_id, evnt):
    """
    Inserts a new event to the Google Calendar, from the user input.

    @param cal(resource): The calendar being called
    @param c_id(str): Google Calendar ID
    @param evnt(dict): Event inserted into calendar
    """
    cal.events().insert(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        sendNotifications=True, body=evnt
    ).execute()
