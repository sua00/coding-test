def solution(n, t, m, p):
    answer = ''
    total = ''
    num = 0
    def convert(num,n):
        digits = "0123456789ABCDEF"
        result = ""
        
        if num ==0:
            return "0"
        
        while num >0:
            remainder = num%n
            result = digits[remainder]+result
            num = num//n
        return result
    
    while len(total) < m*t:
        total += convert(num,n)
        num+=1
    
    for i in range(t):
        index = (p-1) + (i*m)
        answer += total[index]
        
    return answer