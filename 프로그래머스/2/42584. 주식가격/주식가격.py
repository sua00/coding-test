def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            answer[stack[-1]] = i-stack[-1]
            stack.pop()
            
            
        stack.append(i)
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices)-idx-1
    return answer