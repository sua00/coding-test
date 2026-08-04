from collections import deque
def solution(prices):
    answer = [0]*len(prices)
    temp = []
    
    for i in range(len(prices)):
        while temp and prices[temp[-1]] > prices[i]:
            j = temp.pop()
            answer[j] = i-j
            
        temp.append(i)
    
    while temp:
        j= temp.pop()
        answer[j] = len(prices)-1-j
        
    return answer