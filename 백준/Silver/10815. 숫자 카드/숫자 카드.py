n = int(input())
cards = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

results = []

for target in targets:
    if target in cards:
        results.append(1)
    else:
        results.append(0)

print(*results)
