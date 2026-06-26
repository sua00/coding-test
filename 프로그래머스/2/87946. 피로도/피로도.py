def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited= [False] * n
    
    def dfs(current_fatigue, count):
        nonlocal answer
        answer = max(answer,count)
        
        for i in range(n):
            if not visited[i]:
                if current_fatigue >= dungeons[i][0]:
                    visited[i] = True
                    dfs(current_fatigue-dungeons[i][1], count+1)
                    visited[i]= False 
    dfs(k,0)
    return answer