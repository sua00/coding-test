def solution(skill, skill_trees):
    answer = 0
    candidates = []
    for tree in skill_trees:
        result = ''
        for t in tree:
            if t in skill:
                result = result + t
        candidates.append(result)
    for can in candidates:
        valid = True
        for i in range(len(can)):
            if can[i] != skill[i]:
                valid = False
                break
        if valid:
            answer+=1
    
    return answer