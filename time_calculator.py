def add_time(start, duration_time, week=None):
    weekdays = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}

    # get and split data from strings
    start_array = start.split(' ')
    start_time = start_array[0].split(':')
    am_pm = 'AM'
    duration_time = duration_time.split(':')

    # Add start and duration hours together
    tmp_end_hour = (int(start_time[0]) + int(duration_time[0]))

    # Add 12 hours if PM is given to work with 24h format
    if start_array[1] == 'PM':
        tmp_end_hour += 12

    # Add start and duration_time minutes together
    tmp_end_min = (int(start_time[1]) + int(duration_time[1]))

    # Add an hour if minutes < 59
    if (tmp_end_min > 59):
        tmp_end_hour += 1

    # number of days that will have passed after the duration_time.
    days = int(tmp_end_hour // 24)

    # Calculate the end hour using modulo in a 24h format.
    end_hour = tmp_end_hour % 24

    # Change the 'AM' to 'PM' if the 12th hours is passed.
    if end_hour > 11:
        am_pm = 'PM'

    # Convert back to 12h format ()
    if end_hour > 12:
        end_hour -= 12
    elif end_hour == 0:
        end_hour = 12

    # Calculate the ending minute using modulo.
    end_min = tmp_end_min % 60

    end_time = str(end_hour) + ':' + str(end_min).zfill(2) + ' ' + am_pm

    # add new weekday to string if parameter is filled
    if week is not None:
        week = week.lower()
        weekday_num = weekdays[week]
        new_weekday_num = (days + weekday_num) % 7
        new_week = list(weekdays.keys())[list(weekdays.values()).index(new_weekday_num)]
        end_time += ', ' + new_week.capitalize()

    # if day rolls over change
    if days > 1:
        end_time += ' (' + str(days) + ' days later)'
    elif days > 0:
        end_time += ' (next day)'

    return end_time