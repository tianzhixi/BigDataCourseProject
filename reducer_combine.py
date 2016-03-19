#!/usr/bin/python

import sys

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    Pidm, All = data_mapped
    print Pidm, ",", All
