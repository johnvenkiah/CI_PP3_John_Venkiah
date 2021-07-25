class CalOps:

    def __init__:()




    appointments_result = CAL.events().list(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        timeMin=earliest,
        timeMax=latest,
        singleEvents=True,
        orderBy='startTime'
    ).execute()


                CAL.events().delete(  # pylint: disable=maybe-no-member
                calendarId=CAL_ID,
                eventId=apntmnt_id
            ).execute()


        apntmnt_to_edit = CAL.events().get(  # pylint: disable=maybe-no-member
            calendarId=CAL_ID,
            eventId=apntmnt_id
        ).execute()


    CAL.events().update(  # pylint: disable=maybe-no-member
        calendarId=CAL_ID,
        eventId=apntmnt_id,
        body=apntmnt_to_edit
    ).execute()


            CAL.events().insert(  # pylint: disable=maybe-no-member
            calendarId=CAL_ID,
            sendNotifications=True, body=event).execute()