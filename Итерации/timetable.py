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

#flights2 = {}

#for k,v in flights.items():
    #ampm = convert2ampm(k)
    #title = str(v).title()
    #flights2.setdefault(ampm,title)
    
    #flights2.setdefault(convert2ampm(k),v.title())
#    flights2[convert2ampm(k)] = v.title()

"""this is dict generator"""
flights2 = {convert2ampm(k):v.title() for k, v in flights.items()}


pprint.pprint(flights2)
print()

""" this is list generator example """
#destinations = [dest.title() for dest in flights.values()]
#print(destinations)

'''list generator'''
#flights3 = {}
#for dest in set(flights2.values()):
#    flights3[dest] = [k for k, v in flights2.items() if v == dest]

'''this is complex generator (list generator inside dict generator)'''
flights3 = {dest: [k for k, v in flights2.items() if v == dest]
            for dest in set(flights2.values())}

pprint.pprint(flights3)
print()