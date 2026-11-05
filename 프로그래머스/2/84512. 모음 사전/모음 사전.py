def solution(word):
    answer = 0
    words =[]
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current):
        if len(current) > 5:
            return
        if current:
            words.append(current)
            
        for v in vowels:
            dfs(current+v)
    
    dfs("")
    
    answer = words.index(word)+1
    return answer