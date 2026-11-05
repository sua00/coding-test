def solution(n, wires):
    answer = n
    
    for idx in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        
        for i, (a,b) in enumerate(wires):
            if i == idx:
                continue
            
            graph[a].append(b)
            graph[b].append(a)
    
        visited = [False] * (n+1)

        def dfs(node):
            visited[node] = True
            count = 1

            for nxt in graph[node]:
                if not visited[nxt]:
                    count += dfs(nxt)

            return count

        count = dfs(1)

        diff = abs(count - (n-count))
        answer = min(diff, answer)
    return answer