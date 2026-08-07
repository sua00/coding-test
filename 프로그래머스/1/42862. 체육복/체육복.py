def solution(n, lost, reserve):
    answer = 0
    #여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다. -> 이런 제약 사항 먼저 처리
    #[a,b][a,b,c] : a는 여벌 없는 거임
    common = set(lost)&set(reserve)
    lost = sorted(set(lost) - common)
    reserve = sorted(set(reserve) - common)
    for r in reserve:
        if (r-1) in lost:
            lost.remove(r-1)
        elif (r+1) in lost:
            lost.remove(r+1)
    answer = n-len(lost)
    return answer