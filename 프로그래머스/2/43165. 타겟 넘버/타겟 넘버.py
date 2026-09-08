# dfs : 한 가지 경로로 쭉 해보고 답을 확인하는 구조
#dfs : 재귀를 통해 구현

def solution(numbers, target):
    answer = 0
    
    def dfs(index, result):
        nonlocal answer
        
        if index == len(numbers):
            if result == target:
                answer+=1
            return
        
        dfs(index+1, result+numbers[index])
        dfs(index+1, result-numbers[index])
    
    dfs(0,0)
    return answer