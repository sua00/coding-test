def solution(citations):
    citations = sorted(citations, reverse=True)

    
    for i, cit in enumerate(citations):

        if cit < i+1:
            return i
    return len(citations)
    