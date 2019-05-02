#! usr/bin/python3
# Project Euler 12 - looking for first triangle number which has more than 500 dividers
tri_nb = 0  # triangle number
counter = 1
dividers = 1  # liczba dzielnikow
from math import sqrt
while dividers < 500:
    dividers = 1
    prime_factors = []  # tablica czynników pierwszych
    tri_nb = tri_nb + counter
    counter = counter + 1
    # dzl = 1
    # x = 0
    k = 2
    #  print('\n',tri_nb)
    '''while dzl <= tri_nb:
        if tri_nb % dzl == 0:
            #  print(dzl, end=" ")
            x += 1
            dzl += 1
        else:
            dzl += 1
print('\nThe smallest triangle number which has above 50 dividers is:', tri_nb)''' # this part counts everything good, but times too long
    #  print(tri_nb)
    tri_nb2 = tri_nb  # inside tri_nb2 is the largest tri_nb
    while tri_nb2 > 1 and k <= sqrt(tri_nb2):
        while tri_nb2 % k == 0:
            prime_factors.append(k)
            tri_nb2 = tri_nb2 / k
        k += 1
    if tri_nb2 > 1:
        prime_factors.append(tri_nb2)
    for x in prime_factors:
        if prime_factors.count(x) > 1:
            dividers = dividers * (prime_factors.count(x) + 1)
            del prime_factors[0: prime_factors.count(x) - 1]
        else:
            dividers = dividers * (prime_factors.count(x) + 1)
            #  del prime_factors[0]
print(tri_nb, dividers)