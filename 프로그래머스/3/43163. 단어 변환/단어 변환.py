#bfs문제, 최단거리와 유사
from collections import deque

def solution(begin, target, words):
    visited = [False]*len(words)
    answer =0
    queue = deque()
    queue.append((begin, 0))
    while queue:
        start, cnt = queue.popleft()
        if start == target:
            return cnt
        for i in range(len(words)):
            if not visited[i]:
                diff = 0
                for j in range(len(target)):
                    if start[j] != words[i][j]:
                        diff+= 1
                if diff ==1:
                    visited[i] =True
                    queue.append((words[i], cnt+1))
    return 0
            
            
        