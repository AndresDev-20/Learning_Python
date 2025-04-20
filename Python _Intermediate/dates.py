## Dates ##

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(f"Año: {date.year}")
    print(f"Mes: {date.month}")
    print(f"Day: {date.day}")
    print(f"Hora: {date.hour}")
    print(f"Minutos: {date.minute}")
    print(f"Segundos: {date.second}")
    print(f"Timestate: {date.timestamp()}")

print_date(now)

timestam = now.timestamp()

print(timestam)

year_2023 = datetime(2023, 1, 1, 3)

print_date(year_2023)


from datetime import time

current_time = time(21, 3, 2)
print(current_time.hour)
print(current_time.min)
print(current_time.second)


from datetime import date

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 7)
print(current_date.year)
print(current_date.month)
print(current_date.day)
