def solution(s):
    answer = True
    check = []
    
    if s[-1] == '(' or s[0]==')':
        return False
    for c in s:
        if c == '(':
            check.append(c)
        else:
            if not check:
                return False
            check.pop()
    return not check