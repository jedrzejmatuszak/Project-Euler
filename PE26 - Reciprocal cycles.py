#! usr/bin/python3
# Project Euler 26 - Reciprocal cycles
decimal = []
max_len = 0
for x in range(2, 1001):
    y = 1 / x
    y = str(y)
    if max_len < len(y[2:]):
        max_len = len(y[2:])
    decimal.append(y[2:])
for z in range(len(decimal)):
    if len(decimal[z]) == max_len - 3:
       if decimal[z][:int(len(decimal[z])/2)] == decimal[z][int(len(decimal[z])/2):]:
           print(decimal[z])