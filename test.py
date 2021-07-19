class Counter():
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 7

    def decrement(self):
        self.counter -= 7

    def get_value(self):
        return self.counter


mc = Counter()


def count(mc):

    while True:
        gragga = input('choose week: ')
        if gragga == 'n':
            mc.increment()
            week = mc.get_value()
            print(week)

        elif gragga == 'b':
            mc.decrement()
            week = mc.get_value()
            print(week)

        elif gragga == 'e':
            return False
        else:
            print('STROLTCH!')
            week = mc.get_value()
            print(week)


count(mc)
