#!/usr/bin/env python3
import sys

if len(sys.argv) - 1 < 2:
    print("none")
else:
    params = sys.argv[1:]
    for item in reversed(params):
        print(item)
