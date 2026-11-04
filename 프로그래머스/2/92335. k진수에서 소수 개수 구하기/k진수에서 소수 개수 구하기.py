def solution(n, k):
    answer = 0
    def is_prime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    def convert(n,k):
        result = ''
        while n>0:
            result =str(n%k)+result
            n = n//k
        return result
    
    n_k = convert(n,k)
    nums = n_k.split('0')
    
    for num in nums:
        if num =="":
            continue
        if is_prime(int(num)):
            answer +=1
    return answer