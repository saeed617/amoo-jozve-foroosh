import re
from datetime import datetime

from django import template

from apps.utils import jalali

register = template.Library()

JALALI_MONTHS = ['فروردین', 'اردیبهشت', 'خرداد',
                 'تیر', 'مرداد', 'شهریور',
                 'مهر', 'آبان', 'آذر',
                 'دی', 'بهمن', 'اسفند', ]


@register.filter
def jalali_date(date):
    if not isinstance(date, datetime):
        return None
    date = date.strftime('%Y-%m-%d')
    jy, jm, jd = jalali.Gregorian(date).persian_tuple()
    month_name = JALALI_MONTHS[jm - 1]
    return "{day} {month} {year}".format(day=persian_digits(jd), month=month_name, year=persian_digits(jy))


@register.filter
def persian_digits(s):
    s = str(s)
    digits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
    return re.sub(r'0|1|2|3|4|5|6|7|8|9', lambda c: digits[int(c.group())], s)
