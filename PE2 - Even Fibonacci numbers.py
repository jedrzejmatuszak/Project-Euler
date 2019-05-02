#! usr/bin/python3
# Program podaję sume parzystych wartości ciągu fibbonaciego. Wartości nie mogą przekraczać 4mln

counter = 1
even_sum = 0
i = 0
print('Zostanie wypisany ciąg Fibbonaciego do elementu o wartości <= 4mln')
fib = [1]
while fib[i] <= 4 * 10 ** 6:
    counter = fib[i - 1] + fib[i]
    fib.append(counter)
    i = i + 1
fib.remove(fib[i])
# print(fib)
for x in fib:
    if x % 2 == 0:
        even_sum = even_sum + x
print(even_sum)
