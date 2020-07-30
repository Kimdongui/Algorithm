example = [1, 3, 15, 6, 2, 7, 9, 5]


def msort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]
    msort(a1)
    msort(a2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            a[ia] = a1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = a2[i2]
            i2 += 1
            ia += 1
    while i1 < len(a1):
        a[ia] = a1[i1]
        i1 += 1
        ia += 1
    while i2 < len(a2):
        a[ia] = a2[i2]
        i2 += 1
        ia += 1
    
    print(a)

msort(example)

