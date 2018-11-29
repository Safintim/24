def get_time(hour, minute):
    one_hour = 60
    half_day = 12
    if minute == 0:
        if hour == 0:
            print('полночь')
        elif hour == 1 or hour == 13:
            print('час')
        else:
            print(hour)
    elif minute <= 30:
        if hour == 23:
            print('{} минут к полуночи'.format(minute))
        else:
            print('{} минут {}ого'.format(minute, (hour + 1) % half_day))
    else:
        if hour + 1 == 1 or hour + 1 == 13:
            print('без {} час'.format(one_hour - minute))
        elif hour + 1 == 24:
            print('без {} полночь'.format(one_hour - minute))
        else:
            print('без {} {}'.format(one_hour - minute, hour + 1))


get_time(0, 1)
get_time(3, 29)
get_time(12, 12)
get_time(13, 12)
get_time(23, 23)
get_time(0, 31)
get_time(3, 59)
get_time(12, 42)
get_time(23, 32)

