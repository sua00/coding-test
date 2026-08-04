from collections import deque
def solution(priorities, location):
    line = deque(enumerate(priorities))
    order =1
    while line:
        idx, pri = line.popleft()
        if any (pri < p for _,p in line):
            line.append((idx,pri))
        else:
            if idx == location:
                return order
            order+=1

