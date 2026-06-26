# dfs/bfs 중 어느 것을 사용해도 괜찮은 문제
# 단 방문체크가 중요함
def solution(n, computers):
    #컴퓨터 방문했는지 확인
    visited = [False] * n
    answer = 0
    
    def dfs(node):
        visited[node] = True
        
        for next_com in range(n):
            if computers[node][next_com] == 1 and not visited[next_com]:
                dfs(next_com)
    
    for i in range(n):
        if not visited[i]:
            answer+=1
            dfs(i)
    
    return answer