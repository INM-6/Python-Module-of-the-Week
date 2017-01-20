#!/usr/bin/python3
# encoding: utf8

import re

with open("15270/hpc_benchmark-S1-N2.2222-P1-T168.out", 'r') as infile:
    for line in infile:
        print(line.strip('\n'))
