from collections import deque

def solution(progresses, speeds):
    remains = deque()
    remain = 0
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] > 0:
            remain = ((100-progresses[i])//speeds[i])+1
            remains.append(remain)
        else :
            remain = int((100-progresses[i])/speeds[i])
            remains.append(remain)
    
    answer = []
    
    while remains:
        target = remains.popleft()
        cnt =1
        
        while remains and remains[0] <= target:
            remains.popleft()
            cnt+= 1
            
        answer.append(cnt)
        
    return(answer)
    
            
    