#! usr/bin/python3
#  Project Euler 20 - Amicable Numbers
#  Liczby zaprzyjaźnione
def dzielniki(x):
    dzl = []
    k = 1
    while x != k:
        if x % k == 0:
            dzl.append(k)
        k += 1
    return sum(dzl)

suma = 0
a = 220
amicable_numbers = []
while a < 11000 or b < 11000:
    b = dzielniki(a)
    sum_of_b = dzielniki(b)
    if a != b and sum_of_b == a:
        if a not in amicable_numbers or b not in amicable_numbers:
            amicable_numbers.append(a)
            amicable_numbers.append(b)
            print(a, b, sum_of_b)
            suma = suma + a + b
            print('Suma to:', suma,)
    a += 1