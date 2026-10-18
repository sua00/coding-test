#그리디 문제 : 최적의 경우를 선택하기 때문에
# 귤의 크기별로 개수를 count
# 가장 많은 것 부터 선택

from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    counts = Counter(tangerine)
    counts = sorted(counts.values(), reverse = True)
    
    sum_ = 0
    
    for count in counts:
        sum_ += count
        answer +=1
        if sum_ >= k:
            break
    return answer