age = int(input('Please tell me your age: '))

print('You are currently', age, 'years old')

i = 1
while i <= 3:
    num = 10 * i
    my_age = age + num
    print("In ", num, "years, you'll be", my_age, "years old.")
    i += 1