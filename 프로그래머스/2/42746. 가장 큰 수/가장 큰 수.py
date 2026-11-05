def solution(numbers):
    answer = ''
    temp = []
    
    for num in numbers:
        temp.append(str(num)*3)
        
    temp = sorted(temp, reverse =True)
    
    
    for t in temp:
        len_ = len(t)//3
        answer+= t[0:len_]
    
    if answer[0] == '0':
        return '0'
    
    return answer