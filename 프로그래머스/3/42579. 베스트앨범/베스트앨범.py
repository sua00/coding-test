def solution(genres, plays):
    answer = []
    # 먼저 많이 재생된 장르의 순서를 파악해야함
    total = {}
    songs = {} #장르별 음악 정보도 저장해아함

    for i in range(len(genres)):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
            songs[genres[i]] = [(plays[i], i)]
        else:
            total[genres[i]] += plays[i]
            songs[genres[i]].append((plays[i], i))
    
    total = sorted(total, key = lambda x: total[x], reverse = True)
    for genre in total:
        songs[genre].sort(key = lambda x:(-x[0], x[1]))
        for play, idx in songs[genre][:2]:
            answer.append(idx)
    
    return answer