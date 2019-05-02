#! usr/bin/python3
# Project Euler 4 - 906609
pal = []
ns = ''
for x in range(900, 1000):
    for y in range(900, 1000):
        z = x * y
        sn = str(z)
        for m in range(len(sn) - 1, -1, -1):
            ns = ns + sn[m]
        if ns == sn:
            pal.append(z)
        ns = ''
print(max(pal))