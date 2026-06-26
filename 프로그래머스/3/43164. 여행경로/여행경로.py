#최단거리 신호 없으면 : dfs
#답이 여러 개 가능하고, 그중 특정 조건(예: 알파벳 순)으로 하나만 골라야 하는가? dfs+백트레킹
def solution(tickets):
    answer = []
    routes = {} #딕셔너리 형태로 각 공항에서 갈 수 있는 목적지 저리
    for ticket in tickets:
        start, end= ticket[0], ticket[1]
        if start not in routes:
            routes[start]= []
        routes[start].append(end)
        
    for airport in routes:
        routes[airport].sort()
    
    n = len(tickets)
    path=["ICN"]
    
    def dfs(current):
        if len(path) == n+1:
            return True
        if current not in routes:
            return False
        
        for next_airport in routes[current][:]:
            path.append(next_airport) #path 추가
            routes[current].remove(next_airport) #티켓 사용
            
            if dfs(next_airport):
                return True
            
            #실패하면 백트레킹
            path.pop()
            routes[current].append(next_airport)
        return False
    
    dfs("ICN")
    return path