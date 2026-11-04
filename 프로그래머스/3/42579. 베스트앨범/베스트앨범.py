def solution(genres, plays):
    answer = []
    total = {}
    song = {}
    for i in range(len(genres)):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
            song[genres[i]] = [(plays[i], i)]
        else:
            total[genres[i]]+= plays[i]
            song[genres[i]].append((plays[i],i))
            
    total = sorted(total, key = lambda x: total[x], reverse = True)
    for genre in total:
        song[genre].sort(key = lambda x: (-x[0], x[1]))
        
        for play, idx in song[genre][:2]:
            answer.append(idx)
    
    return answer