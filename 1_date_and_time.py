"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, timedelta


def print_days():
    print(datetime.now().strftime("%d/%m/%Y"))
    print((datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y"))
    print((datetime.now() - timedelta(days=30)).strftime("%d/%m/%Y"))


def str_2_datetime(date_string):
    date_object = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_object - timedelta(hours=11, minutes=9, seconds=2.123456)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
