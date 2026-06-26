# dfs/bfs 중 어느 것을 사용해도 괜찮은 문제
# 단 방문체크가 중요함
def solution(n, computers):
    answer= 0
    visited = [False]*n
    def dfs(current):
        visited[current]=True
        for i in range(n):
            if computers[current][i]==1 and not visited[i]:
                dfs(i)
    for i in range(n):
        if not visited[i]:
            answer +=1
            dfs(i)
    return answer
                

                