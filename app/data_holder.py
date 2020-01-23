
import os
import json
logfile = 'logfile.txt'

_data = []

if os.path.exists(logfile):
    with open(logfile,'r') as f:
        for line in f:
            d : dict = json.loads(line)
            _data.append(d)        
else:
    with open(logfile,'w') as f:
        pass


def append(message : dict):
    _data.append(message)
    js = json.dumps(message)
    with open(logfile,'a+') as f:
        f.write(js + '\n')

def view():
    return _data