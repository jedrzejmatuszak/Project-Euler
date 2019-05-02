#! usr/bin/python3
#  summation of all primes below 2mln - sito
#  n = int(input('Do jakiej wartosci dodawac liczby pierwsze: '))
n = 2000000
tab = [2]
for x in range(3, n + 1, 2):  # aby uniknąć sprawdzania dzielenia przez 2 zainplementowano tablice z jedna wartoscia 2
    tab.append(x)             # a pozniej petla for dodano wartosci nieparzyste
print('tablica gotowa\n')
from math import sqrt
counter = 1
dzl = tab[counter]
while dzl <= sqrt(n):         # sprawdzanie do momentu kiedy liczba przez ktora dzilimy jest <= sqrt z tej liczby
    print(dzl)
    for i in range(int(len(tab))):
        if tab[i] == dzl:
            pass
        elif tab[i] % dzl == 0:
            tab[i] = 0
    #  print('tutaj')
    '''while tab.count(0) > 0:   # usuniecie wszystkich zer z listy
        tab.remove(0)'''
    counter += 1
    dzl = tab[counter]
    while dzl == 0:
        counter += 1
        dzl = tab[counter]
print('Suma wszystkich liczb pierwszych ponizej wartosci ', n,'to: ', sum(tab))