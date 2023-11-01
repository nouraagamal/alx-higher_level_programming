#!/usr/bin/python3
import sys
for i in range(99):
    sys.stdout.write("{:d} = 0x{:x}".format(i, i))
