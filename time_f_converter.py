import datetime
from datetime import timedelta


class Time_F_Converter():
    """
    Takes instances of time in string format, converts them to datetime,
    adds time offset if needed and returns as string in defined format.
    @param str_iso(str): Keyword for string in non-readable format
    @param str_pretty(str): Keyword for string in readable format
    @param offset(int): Integer passed for datetime to be modified of needed
    """

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
