#인덱스 처리 -> 큐에 인덱스까지 같이 저장해줘야함
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    
    while queue:
        priority, idx = queue.popleft()
        higher = False
        for q in queue:
            if q[0] > priority:
                higher = True
                break
        if higher:
            queue.append((priority, idx))
        else:
            answer +=1
            
            if idx == location:
                return answer
