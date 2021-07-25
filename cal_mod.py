def apt_list(cal, c_id, start, end):

    appointments_result = cal.events().list(
        calendarId=c_id,
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    return appointments_result


def del_apt(cal, c_id, apt_id):

    cal.events().delete(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        eventId=apt_id
    ).execute()


def get_apt(cal, c_id, apt_id):

    apntmnt_to_edit = cal.events().get(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        eventId=apt_id
    ).execute()
    return apntmnt_to_edit


def updt_apt(cal, c_id, apt_id, apmnt):
    """
    Update the Google Calendar event with the input from the previous
    functions from user.

    @param apntmnt_id(str): Google Calendar event identifier
    @param apntmnt_to_edit: Instance of CAL-resource updating calendar
    """
    cal.events().update(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        eventId=apt_id,
        body=apmnt
    ).execute()


def insrt_apt(cal, c_id, evnt):

    cal.events().insert(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        sendNotifications=True, body=evnt
    ).execute()
