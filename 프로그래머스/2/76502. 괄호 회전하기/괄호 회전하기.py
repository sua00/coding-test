def solution(s):
    answer = 0
    circle_ = s*2
    
    def check_(s):
        temp = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i == '{' or i == '(' or i == '[':
                temp.append(i)
            if i == ']' or i == '}' or i == ')':
                if not temp or temp.pop() != pairs[i]:
                    return False
        return not temp
    
    for i in range(len(s)):
        test = circle_[i:i+len(s)]
        if check_(test):
            answer +=1
        
    return answer