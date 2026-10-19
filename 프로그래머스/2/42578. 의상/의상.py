def solution(clothes):
    answer = 1
    # headgear :2, eyewear:1
    # 1개씩 3 + 2개씩 2 = 5개
    # 각 의상의 종류에 몇 개의 옷들이 있는지 
    closet = dict()
    for cloth in clothes: #O(N)
        if cloth[1] not in closet:
            closet[cloth[1]] =1
        else:
            closet[cloth[1]]+=1
            
    for cnt in closet.values():
        answer *= (cnt+1)
    
    answer= answer-1
    return answer