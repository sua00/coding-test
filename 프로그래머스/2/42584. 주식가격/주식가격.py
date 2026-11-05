#단조 스택
#가장 최근 price보다 다음이 크거나 같으면 수납 -> 아니면 pop
def solution(prices):
    stack = []
    answer = [0]*len(prices)
    
    for i in range(len(prices)): #i =0 / i =1 / i =2 / i=3 / i =4
        
        while stack and prices[stack[-1]] > prices[i]: #false false false true false
            idx = stack.pop() #idx = 2
            answer[idx] = i-idx #[0,0,1,0,0]
        
        stack.append(i) #[0] # [0,1] #[0,1,2] #[0,1,3] #[0,1,3,4]
        
    while stack: #[0,1,3,4]
        idx = stack.pop() #0 1 3 4
        answer[idx] = len(prices)-idx-1 #4 3 1 0 
    
    return answer
        
        
        
    
    