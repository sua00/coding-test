def solution(s):
    answer = []
    s = s[2:-2]

    groups = s.split('},{')

    groups.sort(key = lambda x: len(x.split(',')))
    
    for group in groups:
        for num in group.split(','):
            num = int(num)
            
            if num not in answer:
                answer.append(num)
    return answer