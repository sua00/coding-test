#bfs문제, 최단거리와 유사
from collections import deque

def solution(begin, target, words):
    visited = set() #단어니까 set으로 만드는게 편함
    visited.add(begin)
    
    queue = deque()
    queue.append((begin,0)) #(현재단어, 변환횟수)
    
    while queue:
        current_word, count = queue.popleft()
    
        if current_word == target:
            return count
        
        for word in words:
            if word not in visited:
                diff = 0
                for i in range(len(word)):
                    if current_word[i] != word[i]:
                        diff+=1
                if diff ==1:
                    visited.add(word)
                    queue.append((word, count+1))

    return 0