#! usr/bin/python3
# what is the 10001st prime number?
# prime numbers are divide by 1 and itself
# program prints first 20 prime numbers
number = 2  # first prime number
counter = 0
prime = 0
while counter < 10001:
    for div in range(2, number + 1):
        #  print ('Wynik dzielenia ', number ,'przez', div ,'to: ', number / div)
        if number % div == 0:
            prime = prime + 1
    if prime == 1:
        counter = counter + 1
        print(number, ' TO LICZBA PIERWSZA NR', counter,'!')
    prime = 0
    number = number + 1