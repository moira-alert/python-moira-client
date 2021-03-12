DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

MINUTES_IN_HOUR = 60


def get_schedule(start_hour, start_minute, end_hour, end_minute, disabled_days):
    days = []
    for day in DAYS_OF_WEEK:
        day_info = {
            'enabled': True if day not in disabled_days else False,
            'name': day
        }
        days.append(day_info)
    return {
        'days': days,
        'startOffset': start_hour * MINUTES_IN_HOUR + start_minute,
        'endOffset': end_hour * MINUTES_IN_HOUR + end_minute,
    }
