def solution(elements):
    answer = 0
    circle = elements*2
    temp = set()
    
    for start in range(len(elements)):
        total = 0
        
        for len_ in range(1, len(elements)+1):
            total += circle[start+len_-1]
            temp.add(total)
    
    answer = len(temp)
    return answer