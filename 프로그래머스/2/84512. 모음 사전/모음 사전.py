def solution(word):
    answer = 0
    count= 0
    
    vowels = ['A','E','I','O','U']
    
    
    def dfs(current):
            nonlocal answer, count

            if len(current)>5:
                return 

            if current:
                count+=1

                if current == word:
                    answer= count
                    return

            for v in vowels:
                dfs(current+v)

    dfs("")
    
    return answer