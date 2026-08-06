def solution(n, wires):
    answer = n
    
    def dfs(node):
        visited[node]= True
        count = 1
        
        for next_node in graph[node]:
            if not visited[next_node]:
                count += dfs(next_node)
        return count
    
    for cut_a, cut_b in wires:
        
        graph = [[] for _ in range(n+1)]
        
        for a,b in wires:
            if a ==cut_a and b==cut_b:
                continue
            
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [False]*(n+1)
        count = dfs(1)
        
        answer =min(answer, abs(count-(n-count)))
    return answer