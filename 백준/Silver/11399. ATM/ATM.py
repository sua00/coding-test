n = int(input())
time = list(map(int, input().split()))
time.sort()

prefix =[]
current_sum = 0

for x in time:
    current_sum += x
    prefix.append(current_sum)

ans = sum(prefix)

print(ans)
    