import sys
from collections import deque

input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line: return # 입력이 없으면 종료
        n = int(line)
    except: return

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    # 1. 작년 순위로 그래프 만들기
    team = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[team[i]][team[j]] = True
            indegree[team[j]] += 1

    # 2. 순위 변동 적용
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # a -> b 였으면 b -> a로, b -> a 였으면 a -> b로 뒤집기
        if graph[a][b]:
            graph[a][b], graph[b][a] = False, True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a], graph[a][b] = False, True
            indegree[a] -= 1
            indegree[b] += 1

    # 3. 위상 정렬
    result = []
    q = deque([i for i in range(1, n + 1) if indegree[i] == 0])

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

# 메인 실행부
T_str = input().strip()
if T_str:
    for _ in range(int(T_str)):
        solve()