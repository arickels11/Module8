"""CIS 189
Alex Rickels
Mod 8 topic 4 datetime assignment"""
from _datetime import datetime, timedelta


def half_birthday(year, month, day):
    """
    :param year: year that includes last birthday
    :param month: month of birthday
    :param day: birthday day
    :return: half birthday for most recent birthday year
    """
    bday = datetime(year, month, day)
    half_bday = bday + timedelta(days=184)
    return str(half_bday)


if __name__ == '__main__':
    print(half_birthday(2019, 3, 7))
