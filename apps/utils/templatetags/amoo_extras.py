from datetime import datetime
from apps.utils import jalali

JALALI_MONTHS = ['فروردین', 'اردیبهشت', 'خرداد',
                 'تیر', 'مرداد', 'شهریور',
                 'مهر', 'آبان', 'آذر',
                 'دی', 'بهمن', 'اسفند', ]


def jalali_date(date):
    if not isinstance(date, datetime):
        raise Exception('jalali_date templatetag need datetime object')
    date = date.strftime('%Y-%m-%d')
    jy, jm, jd = jalali.Gregorian(date).persian_tuple()
    month_name = JALALI_MONTHS[jm - 1]
    return "{day} {month} {year}".format(day=jd, month=month_name, year=jy)
