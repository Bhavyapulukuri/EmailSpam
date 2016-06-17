#!usr/bin/python
# vim: set fileencoding=ISO-8859-1:
# _*_ coding: ISO-8859-1 _*_
import email
to = {}
f = open("result.txt","r", encoding = "ISO-8859-1")
for line in f:
    msg22 = email.message_from_string(line)
    for to in email.utils.getaddresses(msg22.get_all("To",[])
       print("To:",to)    
   
