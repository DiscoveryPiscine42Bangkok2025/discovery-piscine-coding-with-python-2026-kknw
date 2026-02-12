#!/usr/bin/env python3
def add_one(x):
    x = x + 1
    return x

num = 5
print("Before calling add_one:", num)

add_one(num)

print("After calling add_one:", num)

# x ใน add_one เป็น local variable ที่มีค่า copy num = 5