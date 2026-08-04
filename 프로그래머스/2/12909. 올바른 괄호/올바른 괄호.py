def solution(s):
    answer = True
    temp = []
    #열린 괄호나 닫힌 괄호 하나만 넣고 닫는걸 만날 때마다 가장 최신 열린 괄호부터 닫아준다 -> lifo
    
    if s[-1] =='(' or s[0] == ')':
        return False
    
    for c in s :
        if c == '(':
            temp.append(c)
        else:
            if temp:
                temp.pop()
    return not temp