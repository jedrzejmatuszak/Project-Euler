#! usr/bin/python3
# Project Euler 14 - Collatz sequence
x = 1  # starting number
max_counter = 0  # max number of terms
while x <= 1000000:
    counter = 1
    n = x  # starting number
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
    if max_counter < counter:
        max_counter = counter
        dict = {}
        dict[x] = max_counter
    # print('Collatz sequnce starts from ', x, 'has ', counter, 'terms')
    x += 1
print('The longest chain produces ', dict.keys())
print(dict)