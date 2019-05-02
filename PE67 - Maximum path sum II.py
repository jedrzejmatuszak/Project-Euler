#! usr/bin/python3
# Project Euler 67 - Maximum path sum II (similar to PE18)
triangle = []
with open('p067_triangle.txt') as file:
    for wiersz in file:
        triangle.append(wiersz.split())
for x in range(-2, -len(triangle) - 1, -1):
    for y in range(len(triangle[x])):
        triangle[x][y] = int(triangle[x][y]) + int(max(triangle[x + 1][y], triangle[x + 1][y + 1]))
print(triangle[0])
