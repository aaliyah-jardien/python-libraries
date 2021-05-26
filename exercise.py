from datetime import datetime, timedelta

dt = datetime.today()

for i in range(10):
    added_date = dt + timedelta(days=14)
    dt = added_date
    print(added_date.strftime("%y-%m-%d"))
