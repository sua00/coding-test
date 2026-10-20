# 롤케이크 자를거임
# 토핑들이 일렬로 -> 토핑 종류 수를 똑같이 나눌 것
#공평하게 못 나눌 수도 있음 -> Return 0
#10^6, 10^4

from collections import Counter

def solution(topping):
    answer = 0
    bro1 = set()
    bro2 = Counter(topping)
    
    for i in range(len(topping)-1):
        bro1.add(topping[i])
        bro2[topping[i]]-=1
        
        if bro2[topping[i]]==0:
            del bro2[topping[i]]
        
        if len(bro2) == len(bro1):
            answer +=1
    
    
    return answer