list = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]
roznice = []
for i in range(1, len(list)):
    if list[i] - list[i - 1] < 0:
        roznice.append(list[i - 1] - list[i])
    else:
        roznice.append(list[i] - list[i - 1])

najdluszy_ciag = []
streak = 1
for i in range(1, len(roznice)):
    if roznice[i] == roznice[i - 1]:
        streak += 1
        if (len(roznice) - 1) == i:
            najdluszy_ciag.append([roznice[i - 1], streak])
    else:
        najdluszy_ciag.append([roznice[i - 1], streak])
        streak = 1

longest = -1
value = -1
for i in range(len(najdluszy_ciag)):
    if najdluszy_ciag[i][1] > value:
        longest = i
        value = najdluszy_ciag[i][1]
print(longest, najdluszy_ciag[longest], "    ", najdluszy_ciag)

length = 0
for i in range(0, longest):
    length += najdluszy_ciag[i][1]
print(length)
print(list[length: (length + najdluszy_ciag[longest][1] + 1)])

ostateczny_ciag = list[length: (length + najdluszy_ciag[longest][1] + 1)]

for i in range(len(ostateczny_ciag)):
    if i == 0:
        mini = ostateczny_ciag[0]
        maxi = ostateczny_ciag[0]
    else:
        print(i, ostateczny_ciag[i], mini, maxi)
        if ostateczny_ciag[i] > maxi:
            maxi = ostateczny_ciag[i]
        if ostateczny_ciag[i] < mini:
            mini = ostateczny_ciag[i]

print(f"Najdłuższy ciąg to {najdluszy_ciag[longest][1] - 1}")



for i in range(len(najdluszy_ciag)):
    if i == 0:
        min_luka = najdluszy_ciag[i][0]
        max_luka = najdluszy_ciag[i][0]
    else:
        if max_luka < najdluszy_ciag[i][0]:
            max_luka = najdluszy_ciag[i][0]
        if min_luka > najdluszy_ciag[i][0]:
            min_luka = najdluszy_ciag[i][0]
print(F"Największa luka to {max_luka}, a najmniejsza {min_luka}")
print(f"Najdłuższy ciąg jest długości {najdluszy_ciag[longest][1] + 1}")
print(f"Fragment zaczyna się od {list[length]} i kończy na {list[(length + najdluszy_ciag[longest][1] + 1) - 1]}")

byly = []

for i in range(len(najdluszy_ciag)):
    dodane = False
    for value in range(len(byly)):
        if najdluszy_ciag[i][0] == byly[value][0]:
            byly[value][1] += najdluszy_ciag[i][1]
            dodane = True
    if dodane == False:
        byly.append(najdluszy_ciag[i])
print(byly)
















