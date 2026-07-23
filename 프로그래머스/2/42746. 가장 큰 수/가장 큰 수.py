def solution(numbers):
    answer = ''
    #numbers를 str으로 바꿔줘야함
    numbers = list(map(str, numbers))
    
    # 정렬 순서를 정하기 위해 문자열을 3번씩 반복하고 비교 : 충분히 늘려서 확인한다
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    if numbers[0]=='0':
        return '0'
    for number in numbers:
        answer += number
    
    return answer