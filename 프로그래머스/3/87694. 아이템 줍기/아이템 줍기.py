# 결국에는 이동 가능한 곳을 1로 못 가는 곳을 0으로 채우고
# 1인 칸으로만 이동하도록 한다
# bfs로 풀면 됨

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 지도의 좌표도 최대 좌표 2배로 설정
    board = [[0]*102 for _ in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        x1 *=2
        x2 *=2
        y1 *=2
        y2 *=2
        
        #사각형 안을 1로 모두 채운다
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                board[x][y]=1
    
    for x1, y1, x2, y2 in rectangle:
        x1 *=2
        x2 *=2
        y1 *=2
        y2 *=2
        
        #사각형 내부만 모두 0으로 모두 채운다
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                board[x][y]=0
    
    #아이템과 캐릭터 시작위치도 모두 두배씩
    startX = characterX*2
    startY = characterY*2
    targetX= itemX*2
    targetY= itemY*2
    
    queue = deque()
    queue.append((startX,startY,0))
    
    visited = [[False]*102 for _ in range(102)]
    visited[startX][startY]=True
    
    dx =[1,-1,0,0]
    dy=[0,0,1,-1]
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x==targetX and y==targetY:
            return distance//2
    
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<102 and 0<=ny<102:
                if board[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny,distance+1))
