def solution(order):
    answer = 0
    stack = []
    next_box = 1
    
    for target in order:
        while next_box <= target:
            stack.append(next_box)
            next_box+=1
    
        if stack and stack[-1] == target:
            stack.pop()
            answer+=1
        else:
            break
    return answer