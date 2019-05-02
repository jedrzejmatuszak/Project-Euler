#! usr/bin/python3
# grid 20x20
array = []
grid = []
with open('grid.txt') as file:
    for wiersz in file:
        array.append(wiersz)
for x in range(20):
    grid.append(array[x].split())
max_poz = 0
max_pio = 0
max_prz = 0
max_prz2 = 0
for i in range(20):
    for j in range(16):
        # sprawdzanie wartości maksymalnej poziomo
        poz = int(grid[i][j]) * int(grid[i][j + 1]) * int(grid[i][j + 2]) * int(grid[i][j + 3])
        if max_poz < poz: max_poz = poz
        # sprawdzanie wartości maksymalnej pionowo
        pio = int(grid[j][i]) * int(grid[j + 1][i]) * int(grid[j + 2][i]) * int(grid[j + 3][i])
        if max_pio < pio: max_pio = pio
#sprawdzenie wartosci max po przekatnej
for i in range(16):
    for j in range(16):
        prz = int(grid[i][j]) * int(grid[i + 1][j + 1]) * int(grid[i + 2][j + 2]) * int(grid[i + 3][j + 3])
        if max_prz < prz: max_prz = prz
for i in range(3, 20):
    for j in range(16):
        prz2 = int(grid[i][j]) * int(grid[i - 1][j + 1]) * int(grid[i - 2][j + 2]) * int(grid[i - 3][j + 3])
        if max_prz2 < prz2: max_prz2 = prz2
print(max(max_poz, max_pio, max_prz, max_prz2))