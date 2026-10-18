#그리디
#가장 작은 값과 가장 큰 값을 계속 비교 : 투 포인터 사용
def solution(people, limit):
    answer = 0
    
    people.sort()
    
    left = 0
    right = len(people)-1
    
    while left <= right:
        if left < right and people[left]+people[right] <= limit:
            answer+=1
            left+=1
            right-=1
        else:
            right -=1
            answer +=1
    return answer