from datetime import datetime

def string_to_date(date_input):
    date = datetime(int(date_input.split()[0].split('.')[2]),
                     int(date_input.split()[0].split('.')[1]),
                     int(date_input.split()[0].split('.')[0]),
                     int(date_input.split()[1].split(':')[0]),
                     int(date_input.split()[1].split(':')[1]),
                     0, 0)
    return date
