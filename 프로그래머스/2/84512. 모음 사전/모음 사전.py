def solution(word):
    answer = 0
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current):
        if current:
            words.append(current)
        
        if len(current) == 5:
            return
        
        for vowel in vowels:
            dfs(current+vowel)
    
    dfs("")
    
    answer= words.index(word)+1
    return answer