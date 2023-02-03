# import locale
# locale.setlocale(locale.LC_ALL, "Uz_uz")
# import time
# import datetime
# import calendar


# st_time = datetime.time(hour=1, minute=30, second=30)
# an_time = datetime.time(hour=0, minute=30, second=)
# print(st_time)


# now = datetime.datetime.now()
# # print(now)
# # print(type(now))
# # print(dir(now))

# day = now.day
# month = now.month
# year = now.year
# print(day)
# print(month)
# print(year)

# user = '02051996'

# user_day = user[:2]
# user_month = user[2:4]
# user_year = user[5:]
# print(day- int(user_day))
# print(user_month)
# print(user_year)


# c = calendar.LocaleHTMLCalendar()

# print(c.formatyear(datetime.date.today().year))

from timeit import Timer

# code = """\
# i = 1
# while i < 10**5:
#    i = i + 1
# """
# t = Timer(stmt=code)
# print("While : \n", t.timeit(number=1000))


