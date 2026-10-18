#최대 공약수와 최소공배수는 종종 문제로 나오므로 알고있자

from math import gcd, lcm

def solution(arr):
    answer = 0
    arr.sort()
    
    lcm_ = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        lcm_ = lcm(lcm_, arr[i])
            
    return lcm_