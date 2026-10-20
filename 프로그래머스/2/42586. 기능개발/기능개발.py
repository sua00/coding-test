def solution(progresses, speeds):
    answer = []
    remain = []
    
    for progress in progresses: #O(N)
        remain.append(100-progress)
    
    days =[]
    for i in range(len(remain)):
        if remain[i] % speeds[i] != 0:
            days.append(remain[i]//speeds[i]+1)
        else:
            days.append(remain[i]//speeds[i])
    
    current_days = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current_days:
            count+=1
        else:
            answer.append(count)
            current_days = days[i]
            count = 1
    
    answer.append(count)
    return answer