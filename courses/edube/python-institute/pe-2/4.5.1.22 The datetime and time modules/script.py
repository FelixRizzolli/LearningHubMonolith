import datetime


dt = datetime.datetime(2020, 11, 14, 14, 53, 00)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))  # 2020/11/04 14:53:00
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))  # 20/November/04 14:53:00 PM
print(dt.strftime("%a, %Y %b %d"))  # Wed, 2020 Nov 04
print(dt.strftime("%A, %Y %B %d"))  # Wednesday, 2020 November 04
print('Weekday: ', dt.strftime("%w"))  # 3
print('Day of the year: ', dt.strftime("%j"))  # 309
print('Week number of the year: ', dt.strftime("%U"))  # 44
