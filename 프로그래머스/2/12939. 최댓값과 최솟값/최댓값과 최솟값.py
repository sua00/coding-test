def solution(s):
    answer = ''
    #문자열을 split해서 int로 저장?
    num_ = s.split(" ") 
    int_ = []
    for n in num_: #O(N)
        int_.append(int(n))
    min_, max_ = min(int_), max(int_) #O(1)
    
    answer = str(min_) + " "+ str(max_)
    return answer