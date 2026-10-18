def solution(s):
    #return 해야하는 값 설정
    count = 0    # 이진 변환 횟수
    zeros = 0    # 제거한 0의 총개수
    while s != "1": #종료 조건 설정
        next_ = ''
        # 1. 이번 문자열에 있는 0의 개수 세기
        for i in s:
            if i =='1':
                # 0 모두 제거
                next_ += i
        zeros += len(s)-len(next_)
        # 3. 남은 문자열 길이를 이진수로 변환하기
        # 힌트: bin(6)[2:] == "110"
        s= bin(len(next_))[2:]
        # 4. 변환 횟수 증가시키기
        count+=1
    return [count, zeros]