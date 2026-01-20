def solution(a, b):
    answer = 0
    a_b = int(str(a)+str(b))
    b_a = int(str(b)+str(a))
    if a_b > b_a:
        answer =a_b
    elif a_b < b_a:
        answer =b_a
    else :
        answer =a_b
    return answer