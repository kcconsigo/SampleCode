import datetime as dt

current_date = dt.date.today()
print(current_date)

date1 = dt.date(2021, 1, 5)
print(date1)

print("Year:", date1.year)
print("Month:", date1.month)
print("Day:", date1.day)

time1 = dt.time(10, 45, 30, 34564)
print(time1)

print("Hour:", time1.hour)
print("Minute:", time1.min)
print("Seconds:", time1.second)
print("Microseconds:", time1.microsecond)

datetime_obj = dt.datetime(2021, 11, 28, 23, 55, 59)
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())

current_datetime = dt.datetime.now()
print(current_datetime)

current_time = dt.datetime.now()
next_new_year = dt.datetime(2021, 1, 1)

time_remaining = next_new_year - current_time
print(type(time_remaining))

current_datetime = dt.datetime.now()
print(current_datetime)

string_date = current_datetime.strftime("%A, %B, %d, %Y")
#string_date = current_datetime.strftime("%a, %b, %-d, %I%p")
print(string_date)

date_string = "21 June, 2021"

date_object = dt.datetime.strptime(date_string, "%d %B, %Y")

print("Date obj:", date_object)