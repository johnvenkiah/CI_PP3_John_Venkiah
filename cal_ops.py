class CalOps:

    def __init__(self, cal, c_id, start, end, apt_id, apmnt):

        self.cal = cal
        self.c_id = c_id
        self.start = start
        self.end = end
        self.apt_id = apt_id
        self.apmnt = apmnt

    def apt_list(cal, c_id, start, end):

        # pylint: disable=maybe-no-member
        
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

        cal.events().update(  # pylint: disable=maybe-no-member
            calendarId=c_id,
            eventId=apt_id,
            body=apmnt
        ).execute()

    def insrt_apt(cal, c_id, evnt):

        CAL.events().insert(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        sendNotifications=True, body=event).execute()
