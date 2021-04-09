import datetime


start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)

def daterange(start, end):
    for n in range((end-start).days):
        yield start + datetime.timedelta(n)

total = 0
for singledate in daterange(start, end):
    if singledate.weekday() == 6 and singledate.day == 1:
        total += 1

print(total)

print(1200//7)        