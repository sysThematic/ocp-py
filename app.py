#!/bin/python3

import time
import requests

url = 'http://10.81.97.31:8000/index.txt'

while(True):
  try:
    r = requests.get(url)
  except requests.exceptions.Timeout as errt:
    print ("Timeout! \n", errt)
  except requests.exceptions.ConnectionError as errc:
    print ("Connection Refused! is web server up?\n", errc)
  except requests.exceptions.RequestException as e:
    # catastrophic error. bail.
    print ("OOps: Something Else...\n",e)
  else:
    print (r.text)

  time.sleep(60)
