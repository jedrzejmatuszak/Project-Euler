#! usr/bin/python3
#Project Euler 17 - number letter counts
#Program zamienia podane liczby na słowa / Program replaces input/defined numbers into words

# ta funkcja usuwa łączniki z liczb
def replace(x):
    x = x.replace(' ', '')
    x = x.replace('-', '')
    return x

# ta funkcja zmienia dwucyfrową liczbę na słowo
def two_digits(x):
    if x[0] == '0':
        y = basic[x[1]]
    elif x[0] == '1':
        y = basic[x]
    elif x[1] == '0':
        y = basic[x]
    else:
        y = basic[x[0] + '0'] + '-' + basic[x[1]]
    return y

# słownik zawierający liczby od 1 - 19 i 20 - 90 (co 10)
basic = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
}
total = 0
for number in range(1, 1001):
    number = str(number)
    if len(number) == 4:
        word = 'one thousand'
    if len(number) == 3:
        if number[1:] == '00':
            word = basic[number[0]] + ' hundred'
        else:
            z = two_digits(number[1:])
            word = basic[number[0]] + ' hundred and ' + z
    if len(number) == 2:
        word = two_digits(number)
    if len(number) == 1:
        word = basic[number]
    word = replace(word)
    print(word)
    total += len(word)
print(total)