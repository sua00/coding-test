def solution(numbers):
    answer = 0
    
    candidates = set() #중복 자동 제거 위함
    visited = [False] * len(numbers)
    
    def dfs(current_num):
        if current_num != "":
            candidates.add(int(current_num))
        
        for i in range(len(numbers)):
            if not visited[i] :
                visited [i] = True
                dfs(current_num+numbers[i])
                visited[i]= False
        
    dfs("")
    
    def is_prime(n):
        if n < 2: 
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    answer= 0
    for candidate in candidates:
        if is_prime(candidate):
            answer+=1
        
    return answer