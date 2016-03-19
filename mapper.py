#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",")
    Pidm=data[0]
    All=data[1:]
    print "{0}\t{1}".format(Pidm, ','.join(All))
