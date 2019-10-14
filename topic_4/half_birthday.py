"""CIS 189
Alex Rickels
Mod 8 topic 4 datetime assignment"""
from _datetime import datetime, timedelta


def half_birthday(year, month, day):
    bday = datetime(year, month, day)
    half_bday = bday + timedelta(days=184)
    return str(half_bday)


if __name__ == '__main__':
    print(half_birthday(2019, 3, 7))
