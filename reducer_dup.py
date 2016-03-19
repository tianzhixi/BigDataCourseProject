#!/usr/bin/python

import sys

oldKey=None
pr=[]

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, All = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, ",", ', '.join(pr)
        oldKey = thisKey;
        pr = []

    oldKey = thisKey
    pr.append(All)

if oldKey != None:
    print oldKey, ",", ', '.join(pr)
