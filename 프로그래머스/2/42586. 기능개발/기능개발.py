#[7,3,9]
import math
def solution(progresses, speeds):
    remains = []
    answer =[]
    for i in range(len(progresses)):
        remain = int(math.ceil((100-progresses[i])/speeds[i]))
        remains.append(remain)
    
    day= remains[0]
    cnt = 1
    
    for i in range(1,len(remains)):
        if day >= remains[i]:
            cnt+=1
        else:
            answer.append(cnt)
            day = remains[i]
            cnt = 1
    answer.append(cnt)
    return answer
 