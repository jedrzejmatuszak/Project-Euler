#! usr/bin/python3
# Project Euler 9
for a in range(100, 1000):
    for b in range(100, 1000):
        if a < b:
            for c in range(100, 1000):
                if b < c:
                    if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                        print(a * b * c)
                        break