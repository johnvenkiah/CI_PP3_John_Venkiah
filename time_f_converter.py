"""
John Venkiah time_f_converter.py - Contains TimeFConverter class
for main file run.py, project FeelGood Physio.

"""
import datetime
from datetime import timedelta


class TimeFConverter:
    """
    Takes instances of time in string format, converts them to datetime,
    adds time offset if needed and returns as string in defined format.

    Names of functions mostly for ease not to mix them up instead of having
    one function for all conversions.

    @param str_iso(str): Keyword for string in non-readable format
    @param str_pretty(str): Keyword for string in readable format
    @param offset(int): Integer passed for datetime to be modified of needed
    """

    def __init__(self, str_iso, str_pretty):
        """
        Set initial values.
        """
        self.str_iso = str_iso
        self.str_pretty = str_pretty

    def iso_to_pretty(self, date, offset):
        """
        Converts 'iso-like' format to 'pretty'.
        """
        date = datetime.datetime.strptime(date, self.str_iso)
        date = date + timedelta(hours=offset)
        return date.strftime(self.str_pretty)

    def pretty_to_iso(self, date, offset):
        """
        Converts 'pretty' format to 'iso-like'.
        """
        date = datetime.datetime.strptime(date, self.str_pretty)
        date = date + timedelta(hours=offset)
        return date.strftime(self.str_iso)

    def add_hour_iso(self, date, offset):
        """
        Converts string to datetime format, adds time offset and
        returns it in the same string format.
        """
        date = datetime.datetime.strptime(date, self.str_iso)
        date = date + timedelta(hours=offset)
        return date.strftime(self.str_iso)
