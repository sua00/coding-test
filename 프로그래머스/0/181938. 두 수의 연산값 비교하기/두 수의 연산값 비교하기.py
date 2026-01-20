def solution(a, b):
    answer = 0
    a_b  = int(str(a)+str(b))
    ab = 2*a*b
    if a_b > ab :
        answer = a_b
    else :
        answer = ab
    return answer