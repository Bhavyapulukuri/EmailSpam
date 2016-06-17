#!/usr/bin/python
import email
from email.utils import getaddresses
file = open("result.txt","r")
count = 0
for line in file:
   msg22 = email.message_from_string(line) 
   for ccs in email.utils.getaddresses(msg22.get_all("cc",[])):
        count += 1
        #print("CC:",ccs)
print("Number of threads are:",count)

   
   

