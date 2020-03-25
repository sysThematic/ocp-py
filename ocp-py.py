#!/bin/python3

import time
import requests

url = 'http://10.81.97.31:8000/index.txt'

while(True):
  try:
    r = requests.get(url)
  except requests.exceptions.Timeout:
    print ("Timeout")
  except requests.exceptions.RequestException as e:
    # catastrophic error. bail.
    raise SystemExit(e)

  print (r.text)
  time.sleep(60)
