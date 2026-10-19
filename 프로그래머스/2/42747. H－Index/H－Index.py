def solution(citations):
    answer = 0
    candidate = []
    for i in range(max(citations)+1):
        temp =0
        for cit in citations:
            if cit >= i: #i회보다 많이 인용됐으면
                temp+=1 #i회보다 많이 인용된 논문 +1
        if i <= temp:
            candidate.append(i)
    answer =max(candidate)
    return answer