def solution(msg):
    answer = []
    dictionary = {}
    
    for i in range(26):
        dictionary[chr(65+i)] = i+1
    
    i = 0
    while i < len(msg):
        w = msg[i]
        j = i+1 #그 다음 알파벳
        
        while j < len(msg) and w+msg[j] in dictionary:
            w = w+msg[j]
            j = j+1
        
        answer.append(dictionary[w])
        
        if j < len(msg):
            dictionary[w+msg[j]] = len(dictionary)+1
        
        i=j
                
    return answer