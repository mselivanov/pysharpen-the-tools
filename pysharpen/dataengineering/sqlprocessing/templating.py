import datetime as dt
import jinja2

from helpers.helpers import print_header

_TEST_TEMPLATE = """
    select *
      from dataset.table
     where date < '{{ macros.format_date(CURRENT_DATE) }}'
       and date > '{{ macros.format_date(macros.add_days(CURRENT_DATE, -7)) }}'
"""


class CustomFunctions:
    @staticmethod
    def format_date(adate: dt.date, format_str='%Y-%m-%d'):
        return adate.strftime(format_str)
    
    @staticmethod
    def add_days(adate: dt.date, days: int):
        return adate + dt.timedelta(days=days)


_GLOBAL_PARAMETERS = {
    'macros': CustomFunctions(),
    'CURRENT_DATE': dt.date.today()
}


def inject_date_functions():
    t = jinja2.Template(source=_TEST_TEMPLATE) 
    s = t.render(**_GLOBAL_PARAMETERS)
    print(s)


def main():
    inject_date_functions() 


if __name__ == '__main__':
    main()