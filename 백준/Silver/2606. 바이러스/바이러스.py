n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range (m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    sorted(graph[i])
    
####

visited = [False]*(n+1)
result = []

def dfs(x):
    visited[x] = True
    result.append(x)
    for next in graph[x]:
        if not visited[next] :
            dfs(next)
dfs(1)
print(len(result)-1)