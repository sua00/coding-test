def solution(n):
    answer = 0
    temp = 0
    
    for i in range(1, n+1): #O(N)
        temp = i
        while temp < n: #O(logN) : i가 커질수록 반복횟수 감소 
            temp += i+1
            i = i+1
        if temp == n:
            answer+=1
    
    return answer