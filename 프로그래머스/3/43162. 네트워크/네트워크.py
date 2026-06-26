# dfs/bfs 중 어느 것을 사용해도 괜찮은 문제
# 단 방문체크가 중요함
def solution(n, computers):
    visited= [False] * n #0,1,2번 컴퓨터에 대해서 방문체크
    answer = 0
    
    def dfs(node):
        visited[node] = True #방문 체크
        for next_node in range(n): #0부터 n-1컴퓨터까지 모두 확인
            if computers[node][next_node] ==1 and not visited[next_node]:
                dfs(next_node)
                
    for i in range(n): #0부터 n-1번 컴퓨터 확인
        if not visited[i]: #아직 방문 안된 컴퓨터 -> 새로운 네트워크
            answer+=1
            dfs(i)
            
    return answer