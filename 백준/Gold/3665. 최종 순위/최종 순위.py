import sys
from collections import deque

input = sys.stdin.readline

def solve():
    try:
        n = int(input().strip())
    except: return

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    team = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(i + 1, n):
            graph[team[i]][team[j]] = True
            indegree[team[j]] += 1

    m = int(input().strip())
    for _ in range(m):
        a, b = map(int, input().split())
        # 원래 어느 방향이었든 반대로 뒤집기
        if graph[a][b]:
            graph[a][b], graph[b][a] = False, True
            indegree[b] -= 1; indegree[a] += 1
        else:
            graph[b][a], graph[a][b] = False, True
            indegree[a] -= 1; indegree[b] += 1

    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(n):
        if not q:
            print("IMPOSSIBLE")
            return
        if len(q) > 1:
            print("?")
            return
        
        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    print(*(result))

T = int(input().strip())
for _ in range(T):
    solve()