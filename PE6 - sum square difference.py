#! usr/bin/python3
# difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
sumsqr = 0
sqrsum = 0
for x in range(1, 101):
    sumsqr = sumsqr + pow(x, 2)
print(sumsqr)
for y in range(1, 101):
    sqrsum = sqrsum + y
sqrsum = pow(sqrsum, 2)
print(sqrsum)
solution = sqrsum - sumsqr
print(solution)