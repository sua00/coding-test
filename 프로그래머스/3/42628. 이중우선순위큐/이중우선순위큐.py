import heapq
def solution(operations):
    answer = []
    h = []
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd =='I':
            heapq.heappush(h, num)
        elif h:
            if num == 1:
                h.remove(max(h))
                heapq.heapify(h)
            else:
                heapq.heappop(h)
    
    if h:
        answer = [max(h), min(h)]
    else:
        answer = [0,0]
    return answer