class Inc_Dec_Week():
    """
    Allows staff navigate between weeks in schedule, by returning
    an integer based on the function called. This way, number will retain value
    after each time function is run.
    Inspiration from this site:
    https://stackoverflow.com/questions/47697945/
    python-how-to-increment-number-and-store-in-variable-every-time-function-runs/
    47698278
    """
    def __init__(self):
        self.inc_dec_week = 0

    def increment(self):
        self.inc_dec_week += 7

    def decrement(self):
        self.inc_dec_week -= 7

    def get_value(self):
        return self.inc_dec_week
