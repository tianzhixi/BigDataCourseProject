#!/usr/bin/python

import sys

oKey=None
ooKey=None
oAll=None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, All = data_mapped
    if oKey!=ooKey and oKey!=thisKey:
        print oKey, ',', oAll

    ooKey = oKey
    oKey=thisKey
    oAll=All
