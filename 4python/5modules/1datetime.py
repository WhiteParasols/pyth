import datetime as dt

#module명.class명.function명()
print(dt.MINYEAR)
print(dt.datetime.now())
print(dt.datetime.now().strftime('%Y-%m-%d'))
print(dt.datetime.now().strftime('%H:%M:%S'))

#특정 날짜 정해서 시간값 담아두려면
my_time=dt.datetime(2025,6,30,10,45,00)
print(type(my_time))
print(my_time)