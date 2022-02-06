#!/usr/bin/python

from time import sleep

secs = 5

print(f'every {secs} seconds will be print hello')
while True:
  sleep(secs)
  print('hello')
