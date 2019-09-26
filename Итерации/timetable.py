from datetime import datetime

import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')



with open('timetable.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}

for k,v in flights.items():
    ampm = convert2ampm(k)
    title = str(v).title()
    flights2.setdefault(ampm,title)
    

pprint.pprint(flights2)
print()
