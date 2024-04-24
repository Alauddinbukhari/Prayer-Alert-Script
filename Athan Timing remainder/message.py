
from datetime import datetime


def message(prayer_name,h24_time):

    d = datetime.strptime(h24_time, "%H:%M")
    h12_time= d.strftime("%I:%M %p")

    return f"Assalamu alaikum wa rahamatuallahi wa barakatuhu\n It's almost {h12_time}, Time for offering {prayer_name} prayer\n leave for prayer"