import datetime

today_date = datetime.datetime.utcnow().strftime("%d/%M/%Y")
print(today_date)
need_date = int(today_date[:2]), (today_date[1:3], today_date[])
# print(type(today_date))
print(need_date)
