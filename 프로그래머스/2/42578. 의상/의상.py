def solution(clothes):
    answer = 1
    closet = {}
    
    for cloth in clothes:
        if cloth[1] not in closet:
            closet[cloth[1]] = 1
        else:
            closet[cloth[1]]+=1
    
    for c in closet:
        answer *= (closet[c]+1)
    answer = answer -1
    return answer