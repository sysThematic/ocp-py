#!/bin/python3

import requests
url = 'http://10.81.97.31:8000/index.txt'
r = requests.get(url)
print (r.text)