#1 usr/bin/python3
#  Project Eulre 22 - Names scores
pct = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
       'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
       'Z': 26}

#  imiona z pliku examp.txt, na którym sprawdzałem działanie programu
#  ANIA - 1+14+9+1 = 25; 25
#  MAGDA = 13+1+7+4+1 = 26; 52
#  MARYSIA = 13+1+18+25+19+9+1 = 86; 258
#  SARA = 19+1+18+1 = 39; 156

with open('names.txt') as file:
    read_data = file.read()
read_data = sorted(read_data.split(','))  # dzieli read_data po przecinku i sortuje alfabetycznie
print(read_data)
count = 1  # wprowadziłem zmienną count, która określa na którym z kolei elemencie działamy
total = 0  # suma wszystkich punktów
for x in read_data:
    score = 0
    for y in x:
        if y in pct:
            score += pct[y]
    score *= count
    count += 1
    total += score
print(total)