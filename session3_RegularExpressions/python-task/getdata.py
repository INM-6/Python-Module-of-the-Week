#!/usr/bin/python3
# encoding: utf8

import re

kv = re.compile(r'([a-zA-Z _]+) *:  *([0-9.]+)[ a-zA-Z]*')

with open("15270/hpc_benchmark-S1-N2.2222-P1-T168.out", 'r') as infile:
    d = dict()
    for line in infile:
        for match in kv.findall(line):
            d[match[0].strip()] = float(match[1])

print(d)
