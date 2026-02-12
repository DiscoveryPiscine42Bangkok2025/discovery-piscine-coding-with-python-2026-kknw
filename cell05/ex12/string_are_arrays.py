#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    num_count = text.count('z')

    if num_count == 0:
        print("none")
    else:
        print('z' * num_count)    
