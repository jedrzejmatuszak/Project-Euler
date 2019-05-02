#! usr/bin/python3
#  Project Euler 20 - silnia
n = 1
silnia = 1
while n <= 100:
    silnia = silnia * n
    if n == 100:
        print(n, '! =', silnia)
        break
    n += 1
suma = 0
for x in str(silnia):
    suma = suma + int(x)
print(suma)