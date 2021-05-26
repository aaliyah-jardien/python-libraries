from datetime import datetime, timedelta

dt = datetime(2021, 5, 26, 9, 25, 46)
# get datetime after 20 days

add_dt = dt + timedelta(days=20)
print(add_dt.strftime("%m-%d-%y %h:%m:%s"))
