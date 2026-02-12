array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = set()
for num in array:
    if num > 5:
        new_array.add(num + 2)

print(array)
print(new_array)