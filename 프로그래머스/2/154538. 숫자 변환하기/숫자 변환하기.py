from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue = deque()
    queue.append((x,0))
    visited = set([x])
    
    while queue:
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        for next_num in [current+n, current*2, current*3]:
            if next_num <= y and next_num not in visited:
                queue.append((next_num, count+1))
                visited.add(next_num)
        
    return -1