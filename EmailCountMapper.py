#!/usr/bin/python3.5
import sys

def read_csv_data():
   data = []
   for line in sys.stdin:
      data.append(line)
   return data

EMAIL_END_MARKER = "#####ES##########ES#####"

def find_num_emails(data):
   for row in data:
     if(EMAIL_END_MARKER in row):
       print("{0}\t{1}".format("Email:",1))

def Main():
 #the_path = raw_input()
   res = read_csv_data()
   find_num_emails(res)

Main()
