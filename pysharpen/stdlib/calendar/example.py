from helpers.helpers import print_header

import calendar
import datetime as dt

def calendar_examples():
    # Create a plain text calendat
    tc = calendar.TextCalendar(calendar.MONDAY) 
    today = dt.date.today()
    month_str = tc.formatmonth(today.year, today.month, 0, 0)
    print(month_str)

    # Create an HTML calendar
    hc = calendar.HTMLCalendar(calendar.MONDAY)
    month_str = hc.formatmonth(today.year, today.month, False)
    print(month_str)

    # Iterate over month and day names using current locale
    for mn in calendar.month_name:
        print(mn)
    for dn in calendar.day_name:
        print(dn)

    # Calculate dates for the first Friday of every month next year
    month_numbers = range(1, 13)
    next_year = today.year+1 
    friday_idx = calendar.FRIDAY
    for m in month_numbers:
        # Returns an array of weeks for every month
        cal = calendar.monthcalendar(next_year, m)
        day = cal[0][friday_idx] if cal[0][4] != 0 else cal[1][friday_idx]
        meeting = dt.date(next_year, m, day)
        print(f'Meeting is on {meeting}')

def main():
    calendar_examples() 


if __name__ == '__main__':
    main()