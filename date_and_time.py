from datetime import datetime, date, time, timedelta

# створення об'єктів часу та дати
dt = datetime.now()
print('Now:' + str(dt))
dt = datetime(2004, 12, 1, 23, 14, 57)
print(dt)

d = date.today()
print('Today: ' + str(d))

d = date(2004, 12, 1)
print(d)

t = datetime.now().time()
print('Current time: ' + str(t))
t = time(23, 14, 57)
print(t)

# вичитка компонентів дати/часу
dt = datetime.now()
print('Year: ' + str(dt.year))
print('Month: ' + str(dt.month))
print('Day: ' + str(dt.day))
print('Hour: ' + str(dt.hour))
print('Minute: ' + str(dt.minute))
print('Second: ' + str(dt.second))
print('Ms: ' + str(dt.microsecond))

# різниця між датами
dt_a = datetime(1983, 1, 5, 13, 45)
dt_now = datetime.now()

diff = dt_now - dt_a # difference
print()
print('Time difference: ' + str(diff))
print('Days: ' + str(diff.days))
print('Seconds: ' + str(diff.seconds))
print('Microseconds: ' + str(diff.microseconds))

print('Total seconds: ' + str(diff.total_seconds()))

# додати або відняти декілька днів від дати
dt_now_plus2days = dt_now + timedelta(days=2)
dt_now_plus2hrs = dt_now + timedelta(seconds=3600*2)
dt_now_plus27min = dt_now + timedelta(seconds=60*27)
dt_now_plus105sec = dt_now + timedelta(seconds=105)
print()
print('Now:' + str(dt))
print()
print('2 days ahead: ' + str(dt_now_plus2days))
print('2 hrs ahead: ' + str(dt_now_plus2hrs))
print('27 minutes ahead: ' + str(dt_now_plus27min))
print('105 seconds ahead: ' + str(dt_now_plus105sec))
