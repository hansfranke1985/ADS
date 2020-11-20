# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:09:46 2020

@author: hansf
"""

import requests

#query on dataset where po = primary schools
r = requests.get('https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/po/', verify = False)
print(r.json())

#save file to disk
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=4)
    
    