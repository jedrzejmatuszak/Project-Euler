#! usr/bin/python3
# Project Euler 1
multiplies_3_and_5 = []
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        multiplies_3_and_5.append(x)
print(sum(multiplies_3_and_5))