#! usr/bin/python3
# Project Euler 16 - Power Digit Sum
power = pow(2, 1000)
print(power)
power = str(power)
sum_of_digits = 0
for x in power:
    sum_of_digits = sum_of_digits + int(x)
print(sum_of_digits)