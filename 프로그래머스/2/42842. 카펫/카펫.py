def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for y in range(3, total+1):
        if total % y== 0:
            x = total//y
            if x>= y and (x-2) * (y-2) == yellow:
                answer = [x,y]
    return answer