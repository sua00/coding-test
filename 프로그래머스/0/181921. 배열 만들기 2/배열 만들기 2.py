def solution(l, r):
    answer = []
    for i in range(l,r+1):
        ok = True
        for j in str(i):
            if j not in ('0','5'):
                ok = False
                break
        if ok:
            answer.append(i)
    return answer if answer else [-1]