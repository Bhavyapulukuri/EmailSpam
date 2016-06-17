#!/usr/bin/python3.5

import sys

def Main():
  data = read_mapper_output()
  find_num_emails(data)

def read_mapper_output():
  data = []
  for line in sys.stdin:
    line = line.strip()
    key, val = line.split("\t",1)
    data.append([key,val])
  return data

def find_num_emails(data):
  num_emails = 0
  for key, val in data:
    num_emails += 1
  
  print("TotalEmails:\t{0}".format(num_emails))

Main()
