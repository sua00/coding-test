import sys
input = sys.stdin.readline

num, goal = map(int, input().split())
coins = [int(input()) for _ in range(num)]

coins.sort(reverse=True)

ans = 0
for coin in coins:
    if goal == 0:
        break
    ans += goal // coin
    goal %= coin

print(ans)
