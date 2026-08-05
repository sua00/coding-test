import heapq
def solution(jobs):
    answer = 0
    #우선순위 : 소요시간이 짧은 것 -> 요청시간이 빠른 것 -> 작업의 번호가 작은 것
    jobs.sort()
    done=0
    n = len(jobs)
    wait = []
    now = 0
    i=0
    total=0
    
    while done < n:
        while i < n and jobs[i][0] <= now:
            heapq.heappush(wait, (jobs[i][1], jobs[i][0]))
            i+=1
        
        if wait:
            time, start= heapq.heappop(wait)
            now += time
            total += now-start
            done += 1
        else:
            now = jobs[i][0]
        
        
    return total//n