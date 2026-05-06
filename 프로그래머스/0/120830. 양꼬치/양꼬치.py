def solution(n, k):
    answer = 0
    lamb = 12000
    coke = 2000
    service = n//10
    answer= (lamb * n) + (coke*(k-service))
    return answer