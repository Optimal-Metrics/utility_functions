# import all the necessary libraries
from datetime import datetime
from pytz import timezone

pacific = timezone('US/Pacific')

def get_epoch_times(date_str, date2=None):
    """
    Convert the input date string to epoch time in milliseconds, 
    and return the start and end of the day in Pacific Time.
    if only one date is provided, epoch_end is for the same date
    if two dates are provided, epoch_end is for the second date
    """
    # Parse the input date string
    date = datetime.strptime(date_str, '%Y-%m-%d')

    # Get the start of the day in Pacific Time
    start_of_day = pacific.localize(datetime(date.year, date.month, date.day, 0, 0, 0))
    epoch_start = int(start_of_day.timestamp() * 1000)

    # if date2 is provided, epoch_end is for date2 
    if date2:
        date = datetime.strptime(date2, '%Y-%m-%d')
        end_of_day = pacific.localize(datetime(date.year, date.month, date.day, 23, 59, 59))
        epoch_end = int(end_of_day.timestamp() * 1000)
    else: # if date2 is not provided, epoch_end is for first date
        end_of_day = pacific.localize(datetime(date.year, date.month, date.day, 23, 59, 59))
        epoch_end = int(end_of_day.timestamp() * 1000)
    
    return epoch_start, epoch_end