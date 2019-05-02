#! usr/bin/python3
# Project Euler 3
n = 600851475143
print('sprawdzam')
pfac = []  # tablica czynnikow pierwszych
pnum = []  # tablica liczb pierwszych
while n > 1:
    for x in range(2, int(n + 1)):
        if n % x == 0:
            if x == 2:
                pfac.append(x)
                n /= x
                break
            for y in range(3, x + 1):
                if x % y == 0:
                    pfac.append(x)
                    n /= x
                    break
print(max(pfac))