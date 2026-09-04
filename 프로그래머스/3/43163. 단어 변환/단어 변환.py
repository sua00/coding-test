from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue = deque()
    visited = [False] * len(words)
    
    queue.append((begin,0))
    
    while queue:
        current, count = queue.popleft()
        
        if current == target:
            return count
        
        for i in range(len(words)):
            if visited[i]==True:
                continue
            
            diff = 0
            for j in range(len(current)) :
                if current[j] != words[i][j]:
                    diff +=1
            
            if diff ==1:
                visited[i]= True
                queue.append((words[i], count+1))
                
    return 0