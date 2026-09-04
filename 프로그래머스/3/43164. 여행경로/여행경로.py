# 한 경로를 끝까지 만들어보고 전체 티켓을 썻는지 확인 -> dfs
def solution(tickets):
    answer = []
    tickets.sort() #알파벳 순으로 방문
    
    visited = [False]*len(tickets) #티켓 사용 여부가 중요
    route = ["ICN"] #시작점 고정
    
    def dfs(current): #내가 현재 있는 공항
        if len(route) == len(tickets)+1: #모든 티켓을 다 사용한 경우
            return True #여행 경로 완성
        
        for i in range(len(tickets)):
            start, end = tickets[i]
            
            if start == current and not visited[i]: #현재 공항에서 출발하면서 아직 사용하지 않은 티켓
                visited[i]= True
                route.append(end)
                
                if dfs(end):
                    return True #이경로로 쭉 갔더니 여행 경로 완성 가능
                
                route.pop() #아닌 경우는 이 길로 그만 가기
                visited[i] = False #티켓 사용도 무르기
        return False
    
    dfs("ICN")
    
    return route