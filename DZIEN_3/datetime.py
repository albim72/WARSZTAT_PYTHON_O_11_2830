import datetime

from datetime import time as tm, date
import time


dt_object = datetime.datetime.now()
print(dt_object)

date_object = date.today()
print(date_object)

print(dir(datetime))

print(f"minimalny rok daty:{datetime.MINYEAR}")
print(f"maksymalny rok daty:{datetime.MAXYEAR}")

print(f"zadeklarowana data: {datetime.date(1966,8,13)}")

print(f"dolna granica daty: {date.min}")
print(f"górna granica daty: {date.max}")

print(f"data liczona od TS w [s]: {date.fromtimestamp(1)}")
obj = time.gmtime(0)
print(obj)
epoka = time.asctime(obj)
print(epoka)
time_sec = time.time()
print(time_sec)

a = tm(11,53,34,2)
print(f"godzina: {a.hour}")
print(f"godzina: {a.minute}")
print(f"godzina: {a.second}")
print(f"godzina: {a.microsecond}")
