n = int(input())

strings =[]
for _ in range(n):
    strings.append(input())

def sum_num(x):
    sum = 0
    for i in x:
        if i.isdigit() == True:
            sum += int(i)
    return sum

strings.sort(key = lambda x:(len(x), sum_num(x), x))

for i in strings:
    print(i)