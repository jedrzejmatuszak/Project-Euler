#! usr/bin/python3
# Project Euler 27
primes = []
for n in range(80):
    if n * n - 79 * n + 1601 not in primes:
        primes.append(n * n - 79 * n + 1601)
print(primes)
print(len(primes))