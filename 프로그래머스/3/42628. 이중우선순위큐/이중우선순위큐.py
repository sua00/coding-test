import heapq
def solution(operations):
    alive = {}
    min_h = []
    max_h = []
    
    for i, operation in enumerate(operations):
        cmd, num = operation.split(" ")
        num = int(num)
    
        if cmd =="I":
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            alive[i] = True
        
        elif cmd =="D":
            if num == 1:
                #min_h에서 삭제된 원소들 정리
                while max_h and not alive[max_h[0][1]]:
                    heapq.heappop(max_h)
                
                if max_h:
                    value, idx = heapq.heappop(max_h)
                    alive[idx] = False
                    
            elif num == -1:
                #max_h에서 삭제된 원소들 정리
                while min_h and not alive[min_h[0][1]]:
                    heapq.heappop(min_h)
                
                if min_h:
                    value, idx = heapq.heappop(min_h)
                    alive[idx] = False
                    
    while max_h and not alive[max_h[0][1]]:
                heapq.heappop(max_h)
                
    while min_h and not alive[min_h[0][1]]:
                heapq.heappop(min_h)
                
    if not min_h:
        return [0,0]
    else:
        return [-max_h[0][0], min_h[0][0]]
