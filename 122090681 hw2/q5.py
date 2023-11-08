l = list()
for i in range(100):
    l.append(True)
for i in range(100):
    j = i
    while j<=99:
        l[j]= not l[j]
        j = j + i + 1
for i in range(100):
    if l[i]: print(i+1)