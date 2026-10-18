#회전시키는 문제 : 2배시켜서 연결시킴
def solution(s):
    answer = 0
    circle = s*2
    
    def check_(s):
        temp = []
        pairs = {')': '(', ']': '[','}': '{'}
        
        for i in s:
            if i == '[' or i == '{' or i == '(':
                temp.append(i)
            else:
                if not temp:
                    return False
                elif temp[-1] != pairs[i]:
                    return False
                else:
                    temp.pop()
                    
        return not temp
            
    for i in range(len(circle)-len(s)):
        target = circle[i:i+len(s)]
        if check_(target):
            answer +=1
        
    return answer