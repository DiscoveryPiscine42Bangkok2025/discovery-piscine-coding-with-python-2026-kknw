#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("none")
        sys.exit
    
    numbers = list(range(num1, num2 + 1))
    print(numbers)
    
        
