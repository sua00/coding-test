#문자열을 갱신시키고, 문자의 길이를 갱신시키고
#필요한 작업들이 많아 혼란이 생겼던 문제
#이진 계산 tool도 기억해두기

def solution(s):
    answer = []
    count, zeros = 0,0
    
    while s != '1':
        next_ = ''
        for i in s:
            if i == '1':
                next_ += i
        count +=1
        zeros += len(s) - len(next_)
        s = bin(len(next_))[2:]
        
    answer = [count, zeros]
    return answer