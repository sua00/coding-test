num = int(input())
strings = []

for _ in range(num):
    strings.append(input())

for s in strings:
    l = list(s)          
    n = len(l)

    pivot = -1
    for i in range(n-2, -1, -1):
        if l[i] < l[i+1]:
            pivot = i
            break

    if pivot == -1:
        l = l

    else:
        for j in range(n-1, pivot, -1):
            if l[j] > l[pivot]:
                l[pivot], l[j] = l[j], l[pivot]
                break
        l[pivot+1:] = sorted(l[pivot+1:])

    print("".join(l))
