#! usr/bin/python3
# Project Euler 13
suma = 0
for wiersz in open('100digit.txt'):
    print(wiersz)
    suma = suma + int(wiersz)
print(str(suma)[:10])