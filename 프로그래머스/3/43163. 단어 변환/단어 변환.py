# 한 번 변환 할 때 비용이 1이므로 bfs 사용하기 적절
# 현재 단어에서 한 글자만 다른 단어로 이동 가능
from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue = deque()
    queue.append((begin,0)) # 시작 단어 추가
    
    visited = [False]*len(words) #방문 처리
    
    while queue:
        current, count = queue.popleft()
        
        if current == target: #현재 단어가 target 이면 count 값 바로
            return count
        
        for i in range(len(words)):
            if visited[i]== True: #이미 방문했으면 다음
                continue
                
            diff = 0
            
            for j in range(len(current)):
                if current[j] != words[i][j]: #현재 단어와 한글자만 다른 경우
                    diff+=1
            
            if diff==1:
                visited[i]= True #방문
                queue.append((words[i], count+1))

    return 0