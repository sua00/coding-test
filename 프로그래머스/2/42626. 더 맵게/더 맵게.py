import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >=2:
        if scoville[0] >= K:
            return answer
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix_ = first+(second*2)
        
        heapq.heappush(scoville, mix_)
        answer +=1
    
    if scoville[0]>=K:
        return answer
        
    return -1