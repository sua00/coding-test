#LIFO를 사용해야함 : stack
#닫힘 괄호를 만났을 때 가장 최근의 여는 괄호를 pop 해야하므로
def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
        
    if stack:
        return False
    else:
        return True