def solution(dirs):
    answer = 0
    x,y = 0,0,
    moves = {
        'U':(0,1),
        'D':(0,-1),
        'L':(-1,0),
        'R':(1,0)
    }
    
    visited = set()
    
    for d in dirs:
        dx,dy = moves[d]
        
        nx = x+dx
        ny = y+dy
        
        if not (-5<=nx<=5 and -5<=ny<=5):
            continue
            
        visited.add((x,y,nx,ny))
        visited.add((nx,ny,x,y))
        
        x,y = nx, ny
    
    answer =len(visited)//2
    return answer