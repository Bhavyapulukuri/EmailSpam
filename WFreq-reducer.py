#!/usr/bin/python
import sys
wordfreq ={}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t",1)
    try:
        count =int(count)
    except:
        continue
    if not wordfreq.get(word):
        wordfreq[word] = 0
    wordfreq[word] += count
for key,val in wordfreq.iteritems():
    print("{0}\t{1}".format(key,val))
