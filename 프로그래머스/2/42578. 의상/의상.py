def solution(clothes):
    answer = 1
    closet = {}
    for a,b in clothes:
        closet[b] = closet.get(b,0)+1
    
    for i in closet:
        answer *= (closet[i]+1)
    answer = answer -1
        
    return answer