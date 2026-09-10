from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            nums.add(int("".join(p)))
    
    for num in nums:
        is_prime = True
        
        if num <2:
            continue
        
        for i in range(2,int(num**0.5)+1 ):
            if num%i ==0:
                is_prime = False
                break
        if is_prime:
            answer+=1
    return answer