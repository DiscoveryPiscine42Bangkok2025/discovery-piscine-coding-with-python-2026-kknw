#!/usr/bin/env python3
import sys

count = len(sys.argv) - 1

if count == 0:
    print("none")
else:
    print("pararmeter:", count)
    for param in sys.argv[1:]:
        print(param + ":", len(param))
