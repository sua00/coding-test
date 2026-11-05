import heapq
def solution(jobs):
    answer= 0
    time = 0
    task = [] #실제 요청된 job들 넣을 곳
    
    #도착 시간 별
    jobs = sorted(
        [(job[0], job[1],i ) for i, job in enumerate(jobs)]
    )
    print(jobs)
    
    idx = 0
    #모든 작업들 할 때 동안 + task 남아 있는 동안
    while idx < len(jobs) or task: 
        
        #현재 시간까지 요청된 task -> task 에 넣음
        while idx < len(jobs) and jobs[idx][0] <= time:
            request, duration, number = jobs[idx]
            heapq.heappush(task, (duration, request, number))
            idx += 1
        
        #요청된 작업이 있는 경우 
        if task:
            duration, request, number = heapq.heappop(task)
            time += duration
            answer += time - request
        else:
            time = jobs[idx][0]
    
    return answer // len(jobs)
        