import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    remain = deque()
    for i in range(len(progresses)):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))
    
    print(remain)
    while remain:
        cur = remain.popleft()
        cnt=1
        print(remain)
        while remain and remain[0]<= cur:
            remain.popleft()
            cnt+=1
        answer.append(cnt)
    return answer