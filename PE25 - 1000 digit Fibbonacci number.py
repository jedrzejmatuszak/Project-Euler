#! usr/bin/python3
# Project Euler 25
fib = [1, 1]
for x in range(2, 4900):
    #  print(fib[x - 1], fib [x - 2])
    fib.append(fib[x - 1] + fib[x - 2])
    if len(str(fib[x])) == 1000:
        print(x)
        break
print(x + 1)