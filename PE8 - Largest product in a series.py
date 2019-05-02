#! usr/bin/python3
# 1000-digit
tab = []
suma_wierszy = 0
array = []
thirteen = {}  # dictionary which storage thirteen adjacent digits
s = ''
key = ''
product = 1
counter = 0
for wiersz in open('digit.txt'):  # odczytywanie wiersz po wierszy pliku digit.txt
    tab.append(wiersz)            # i zapisanie tego do tablicy tab
    suma_wierszy = suma_wierszy + 1
liczba_elementow = len(wiersz)
for x in range(suma_wierszy):     # połączenie elementów tablicy tab w pojedyncze elementy w tablicy array
    for y in range(liczba_elementow - 1):
        array.append(tab[x][y])
print(array)
# kod w potrojnym cudzyslowie pozwala zlaczyc wszystkie elementy tablicy w jeden
"""array = s.join(array)
print(array)
print(len(array))"""
# zliczanie kolejnych elementów tablicy array
for x in range(len(array)):
    if x > len(array) - 13:
        break
    while len(key) < 13:
        key = key + str(array[x])
        product = product * int(array[x])
        x = x + 1
    thirteen[key] = product
    key = ''
    product = 1
print(max(thirteen.values()))