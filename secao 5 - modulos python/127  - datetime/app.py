from datetime import datetime
from datetime import timedelta


data = datetime(year=2021, month=6, day=26, hour=20, minute=53, second=20)
print(data)
formated_data = data.strftime('%d/%m/%Y %H:%M:%S')
print(formated_data)

print('\n')

data = datetime.strptime('26/06/2021', '%d/%m/%Y')
print(data)
tstamp = data.timestamp()
print(tstamp)

print('\n')

data = datetime.fromtimestamp(tstamp)
print(data)

print('\n')

data = data.strptime('26/06/1988 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

print('\n')

d1 = data.strptime('26/06/1988 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = data.strptime('29/06/1988 22:02:20', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(dif.days)

print('\n')

print(d1.time())

