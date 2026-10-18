#짝을 지어서 제거한다는 점에서 괄호 문제와 비슷하다

def solution(s):
    str_ = []
    str_.append(s[0])

    for i in range(1, len(s)):
        if not str_ or s[i] != str_[-1]:
            str_.append(s[i])
        else:
            str_.pop()
    
    if not str_:
        return 1
    else:
        return 0
