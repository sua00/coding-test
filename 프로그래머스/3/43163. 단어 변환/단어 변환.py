# 가장 짧은 변환 과정 찾기 : bfs

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue = deque()
    queue.append((begin,0))
    visited = [False]*len(words)
    
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        
        for i in range(len(words)):
            if visited[i]==False:
                diff =0
                
                for j in range(len(current)):
                    if words[i][j] != current[j]:
                        diff+=1
                        
                if diff == 1:
                    visited[i]=True
                    queue.append((words[i],count+1))
    
    return 0