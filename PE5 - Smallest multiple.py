#! usr/bin/python3
# smallest number evenly divisible from 1 to 20
# https://www.matemaks.pl/algorytm-wyznaczania-nww.html - ten algorytm
from math import sqrt
temp = []
tab_dzl = []
for x in range(2, 21):  # podział na czynniki pierwsze liczb od 2 do 20
    k = 2
    temp.append(x)
    #  print('\n', x,': ', end='')
    while x > 1 and k <= sqrt(x):
        while x % k == 0:
            #  print(k, end=' ')
            temp.append(k)
            x = x / k
        k = k + 1
    if x > 1:
        #  print(x)
        temp.append(x)
    tab_dzl.append(temp)
    temp = []
for x in range(len(tab_dzl)):  # usuniecie pierwszego elementu - liczby rokladanej na czynniki pierwsze
    del tab_dzl[x][0]
slow = {}
for x in range(len(tab_dzl)):  # liczby 2-20 rozlozone na czynniki pierwsze
    print(tab_dzl[x])
    for z in tab_dzl[x]:
        #  print(z)
        """if slow.keys() is True:
            temp = slow.get(str(z))
        wynik = tab_dzl[x].count(z)
        if temp < wynik:"""  # JAK OTRZYMAC WYNIK ILE JEST NAJWIECEJ DANYCH ELEMENTOW???
        slow[z] = tab_dzl[x].count(z)
        #  print(slow)
    """for w in range(1, len(tab_dzl[x])):
        print(tab_dzl[x][w])  """# ten fragment przechodzi przez elementy wewnatrz tab_dzl - aktualnie nie potrzebny
print(slow)