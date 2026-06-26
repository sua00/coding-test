#출발점에서 목적지까지 가장 빨리 가는 길 찾기 : bfs
#가까운 곳 부터 살펴보다가 운좋게 거기 도착점이면 끝! 그렇기 때문에 bfs
from collections import deque

def solution(maps):
    queue = deque()
    queue.append((0,0))
    maps[0][0]=1
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    n = len(maps)
    m = len(maps[0])
    
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if (0<=new_row<n) and (0<=new_col<m):
                if maps[new_row][new_col] == 1:
                    maps[new_row][new_col] = maps[row][col]+1
                    queue.append((new_row, new_col))
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1
    
