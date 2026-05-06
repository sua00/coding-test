def solution(s):
    check = []
    open = "("
    answer = True
        
    for i in s:
        # if (s[0] != open) or (s[-1]== open):
        #     answer = False
        #     break
        if i == open:
            check.append(i)
        else:
            if not check:
                answer = False
            else:
                check.pop()
    if check:
        answer = False
        
    return answer

    
                
            


        