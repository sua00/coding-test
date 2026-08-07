def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    #여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
    common = lost & reserve
    lost = set(lost) -common
    reserve = set(reserve)-common
    
    #체육복 빌려주기
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    answer= n-len(lost)
    return answer