# Write your code here
import json
import re
from datetime import datetime

a = input()
info = json.loads(a)
stops = set()
stopnames = {}
print('On demand stops test:')
for i in info:
    # stopnames[i['stop_id']] = i['stop_name']
    stops.add(i['stop_name'])

def typ(a):
    types = []
    for i in info:
        if i['stop_name'] == a:
            types.append(i['stop_type'])
    return types
wrongs = []
for i in stops:
    if ('O' in typ(i)) and ((typ(i)).count('O') < len(typ(i))):
        wrongs.append(i)
if len(wrongs) != 0:
    print(f'Wrong stop type: {sorted(wrongs)}')
else:
    print('OK')
