def solution(land):
    answer = 0

    for i in range(1,len(land)):
        for j in range(4):
            best = 0
            
            for k in range(4):
                if j!=k:
                    best = max(best, land[i-1][k]+land[i][j])
            land[i][j] = best
    answer = max(land[len(land)-1])

    return answer