def solution(genres, plays):
    answer = []
    genre_chart= {}
    song_chart = {}
    
    for i in range(len(genres)):
        genre_chart[genres[i]] = genre_chart.get(genres[i],0)+plays[i]
        song_chart.setdefault(genres[i], []).append([plays[i],i])
    
    print(song_chart)
    genre_chart = sorted(genre_chart, key = genre_chart.get, reverse = True)
    for g in genre_chart:
        song_chart[g].sort(key = lambda x:(-x[0],x[1]))
        for s, idx in song_chart[g][:2]:
            answer.append(idx)
    
        
    return answer