"""
@author: Maksim Selivanau
Module contains examples on using standard date, datetime, time, timedelta classes
"""
import datetime as dt
from helpers.helpers import print_header

def main():
    date_examples() 
    datetime_examples()
    timedelta_examples()


def datetime_examples():
    print_header('Datetime examples')
    # Get current date and time
    datetime = dt.datetime
    now = datetime.now()
    print(f'Now is: {now}')
    
    time_now = datetime.time(now)
    print(f'Time now is: {time_now}')

    # Format using strftime function
    # %Y - year, %m - month (1-12), %d - day of month(1-31)
    # %b - short month abbreviation (Jan-Dec), %B - full month name
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    # %a - abbreviated day name, %A - full day name
    # %I/%H - 12/24 hour format, %M - minute, %S - second, %p - locale's AM/PM format
    print("Today using locale's date and time format", now.strftime('%c'))
    print("Time using 12 hour and AM/PM format", now.strftime('%I %p'))



def date_examples():
    print_header('Date examples')
    # Print today's date    
    date = dt.date
    today = date.today()
    print(f'Today is: {today}')

    # Print date components: year, month, day of month
    print(f'Year: {today.year}, month: {today.month}, day: {today.day}')
    
    # Print weekday where 0==Monday, 6==Sunday
    print(f'Weekday is: {today.weekday()}')

    # Format using strftime function
    # %Y - year, %m - month (1-12), %d - day of month(1-31)
    # %b - short month abbreviation (Jan-Dec), %B - full month name
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    # %a - abbreviated day name, %A - full day name
    print('Today using dd-mm-yyyy format', today.strftime('%d-%m-%Y'))
    print("Today using locale's date format", today.strftime('%x'))


def timedelta_examples():
    print_header('Timedelta examples') 
    from datetime import timedelta, datetime
    td = timedelta(days=365, hours=10, minutes=2)
    print(f'Timedelta 365 days {td}')
    now = datetime.now()
    year_from_now = now + timedelta(days=365)
    print(f'Year from now {year_from_now}')
    print(f'In 3 weeks and 2 days it will be {now + timedelta(weeks=3, days=2)}')


if __name__ == '__main__':
    main()