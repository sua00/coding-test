def solution(s):
    answer = True
    
    if s[0] == ')':
        answer = False
    if s[-1] =='(':
        answer = False
    
    str_ = []
    for i in s:
        if i == '(':
            str_.append(i)
        else:
            if not str_:
                answer=False
                return answer
            else:
                str_.pop()
    
    if not str_:
        answer= True
    else:
        answer = False
        
    return answer