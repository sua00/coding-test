from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

#그래프 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호부터 방문해야 하므로 정렬
for i in range(1, n+1):
    graph[i].sort()

#BFS
visited_bfs = [False]*(n+1)
bfs_result = []

queue = deque([v])
visited_bfs[v] = True

while queue:
    x = queue.popleft()
    bfs_result.append(x)
    for next in graph[x]:
        if not visited_bfs[next]:
            visited_bfs[next] = True
            queue.append(next)
#DFS
visited_dfs = [False]*(n+1)
dfs_result = []

def dfs(x):
    visited_dfs[x]=True
    dfs_result.append(x)
    for next in graph[x]:
        if not visited_dfs[next]:
            dfs(next)

dfs(v)

print(*dfs_result)
print(*bfs_result)