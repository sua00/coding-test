def solution(participant, completion):
    count = {} 
    # 참가자 이름을 dict에 +1씩
    for p in participant: 
        count[p] = count.get(p, 0) + 1 
        # 완주자 이름을 dict에서 -1씩
    for c in completion: count[c] -= 1
    # 값이 1 남은 사람이 미완주자
    for name, cnt in count.items():
        if cnt == 1:
            return name
        
    
                
    