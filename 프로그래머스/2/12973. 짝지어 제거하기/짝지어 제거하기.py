def solution(s):
    answer = -1
    temp = []
    
    for i in s:
        if temp and temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)
    if temp:
        answer = 0
    else:
        answer = 1
    return answer