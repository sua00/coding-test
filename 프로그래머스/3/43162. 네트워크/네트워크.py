# 경로 끝까지 가서 모두 연결되어있는 덩어리가 몇 개인지 확인하는 거 -> dfs
def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def dfs(current):
        if not visited[current]:
            visited[current]=True
            
            for next_computer in range(n):
                if computers[current][next_computer] == 1 and not visited[next_computer]:
                    dfs(next_computer)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
            
    return answer