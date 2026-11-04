from collections import Counter
def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
   
    answer = list(p-c)[0]
    return answer