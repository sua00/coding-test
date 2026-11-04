from collections import Counter

def solution(str1, str2):
    answer = 0
    def make_pairs(s):
        s = s.lower()
        result =[]
        
        for i in range(len(s)-1):
            pair = s[i:i+2]
            
            if pair.isascii() and pair.isalpha():
                result.append(pair)
        return result
    
    a= Counter(make_pairs(str1))
    b = Counter(make_pairs(str2))
    
    intersection = sum((a&b).values())
    union = sum((a|b).values())
    
    if union == 0:
        answer = 65536
    else:
        answer = int(intersection/union * 65536)
    return answer