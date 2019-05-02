#! usr/bin/python3
# The script shows the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
number = 20
x = 1
while x != 18:
    x = 1
    while number % x == 0:
        print(number, x)
        x = x + 1
        if x == 18:
            print(number)
            print('break')
            break
    number = number + 1

