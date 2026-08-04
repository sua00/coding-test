from collections import deque
def solution(priorities, location):
    order = 0
    answer = 0
    queue_ = deque(enumerate(priorities))
    while queue_:
        idx, pri = queue_.popleft()
        if any(p>pri for q,p in queue_):
            queue_.append((idx,pri))
        else:
            order +=1
            if idx==location:
                return order