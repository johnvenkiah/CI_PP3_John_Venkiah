"""
inc_dec_week.py, imported in main file run.py for use in week_nav_fn.
"""


class IncDecWeek:
    """
    Allows staff to navigate between weeks in schedule, by returning
    an integer based on the function called. This way, number will retain value
    however many times the function is run.
    Inspiration from here:

    https://stackoverflow.com/questions/47697945/
    python-how-to-increment-number-and-store-in-variable-every-time-function-runs/
    47698278
    """
    def __init__(self):
        self.inc_dec_week = 0

    def increment(self):
        """
        Adds 7 to the value.
        """
        self.inc_dec_week += 7

    def decrement(self):
        """
        Subtracts 7 to the value.
        """
        self.inc_dec_week -= 7

    def initialize(self):
        """
        Initializes value to 0.
        """

        self.inc_dec_week = 0
        return self.inc_dec_week

    def get_value(self):
        """
        Gets the value.
        """
        return self.inc_dec_week
