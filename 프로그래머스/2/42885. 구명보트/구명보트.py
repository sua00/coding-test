def solution(people, limit):
    #가장 무거운 사람과 가벼운 사람 태울 수 있으면 태우고 안되면 무거운 사람만
    people = sorted(people)
    left = 0
    right = len(people)-1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left+=1
        
        right-=1
        answer +=1
            
    return answer