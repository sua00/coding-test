def solution(citations):
    answer = 0
    candidate = []

    for i in range(len(citations) + 1):
        temp = 0

        for cit in citations:
            if cit >= i:
                temp += 1

        if temp >= i:
            candidate.append(i)

    answer = max(candidate)
    return answer