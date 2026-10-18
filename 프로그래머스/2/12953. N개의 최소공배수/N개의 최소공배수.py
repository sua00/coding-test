from math import lcm

def solution(arr):
    answer = 0
    arr.sort()
    
    answer = lcm(arr[0],arr[1])
    
    for i in range(2,len(arr)):
        answer = lcm(answer,arr[i])
        
    return answer