from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day

print(now) 
print(year)
print(month)
print(day)

print('%s/%s/%s' % (year, month, day))

print('%s/%s/%s %s:%s:%s' % (now.year,now.month,now.day,now.year,now.month,now.day))