import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()

ans = 0
current = 0

for t in times:
    current += t
    ans += current

print(ans)
