def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer
        
        if index == len(numbers): #끝까지 내려갔을때
            if total == target:
                answer+=1
            return
        
        dfs(index+1, total+numbers[index])
        dfs(index+1, total-numbers[index])
    
    dfs(0,0)
            
    return answer