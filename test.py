
import datetime
GMT_OFF = '+01:00'

def time():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print(now)
    now = datetime.datetime.utcnow().isoformat() + GMT_OFF
    print(now)



time()