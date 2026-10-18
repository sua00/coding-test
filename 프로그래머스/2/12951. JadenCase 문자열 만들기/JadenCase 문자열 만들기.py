def solution(s):
    str_ = s.split(' ')
    answer = ''
    for i in range(len(str_)): #O(N)
        if str_[i]:
            str_[i] = str_[i][0].upper()+str_[i][1:].lower()

    
    return ' '.join(str_)
