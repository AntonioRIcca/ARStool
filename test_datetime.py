import datetime


dt = datetime.datetime.now()

d = dt.replace(year=2024, month=10, day=27, hour=0, minute=0, second=0)
d1 = dt.replace(year=2024, month=10, day=27, hour=0, minute=0, second=0)
d2 = dt.replace(year=2024, month=10, day=28, hour=0, minute=0, second=0)

for i in range(24):
    print(i, d)
    d += datetime.timedelta(minutes=60)

dtime = d2-d1
print(dtime.total_seconds() / 60)

dt.replace(tzinfo=None)