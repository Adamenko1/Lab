x = 38
for i in range(1, x+1):
    il = i
    k = 0
    while i%3 == 0:
        k += 1
        i = i//3
    l = 0
    while i%5 == 0:
        k += 1
        i = i//5
    m = 0
    while i%7 == 0:
        k += 1
        i = i//7
    if i == 1:
        print(il, k,l,m)