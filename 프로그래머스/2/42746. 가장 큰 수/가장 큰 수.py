import string
def solution(numbers):
    answer = ''
    
    numbers = sorted(numbers, key = lambda x: str(x)*3, reverse = True)
    
    for num in numbers:
        answer+= str(num)
    if answer[0] == '0':
        return '0'
    return answer