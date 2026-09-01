#가중치가 없는 그래프에서 최단거리를 구할 때는 bfs가 대표적
#bfs는 파이썬에서 queue로 구현

from collections import deque

def solution(maps):
    answer = 0
    
    #map 모양 설정
    m = len(maps[0]) # m : 열(가로 좌표)
    n = len(maps) #n: 행(세로 좌표)
    
    queue = deque()
    queue.append((0,0)) #시작점 넣기
    
    dx = [-1, 1,0,0]
    dy = [0,0,-1,1] #이동키 설정
    
    while queue:
        x,y = queue.popleft() #현재 위치
        
        for i in range(4): #상하좌우 확인
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m: #maps 범위 안에 속하는 점인지 확인
                if maps[nx][ny] ==1:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx,ny))
    if maps[n-1][m-1] == 1:
            return -1
        
    return maps[n-1][m-1]
            
        
    
    
    return answer