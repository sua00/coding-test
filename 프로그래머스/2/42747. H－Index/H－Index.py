def solution(citations):
    answer = 0
    max_ = max(citations)
    
    for i in range(max_+1):
        count = 0
        for citation in citations:
            if citation >= i:
                count +=1
        if count >= i:
            answer = i
    return answer