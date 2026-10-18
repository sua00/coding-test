def solution(n):
    answer = 0
    temp = 0
    
    for i in range(1, n+1):
        temp = i
        while temp < n:
            temp += i+1
            i = i+1
        if temp == n:
            answer+=1
    
    return answer