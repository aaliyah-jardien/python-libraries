from datetime import datetime, timedelta

dt = datetime(2021, 5, 26, 9, 25, 46)
#get datetime after 10 days
#add_dt = dt + timedelta(days=10)

# get datetime 5 days in past
sub_dt = dt - timedelta(days=5)
print(sub_dt.strftime("%m-%d-%y %h:%m:%s"))
