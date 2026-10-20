#[Jeju, Pangyo, NewYork ]
from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    time = 0
    if cacheSize ==0:
        time = len(cities)*5
        return time
        
    for city in cities:
        city = city.lower()
        
        if city not in cache:
            time+=5
            if len(cache)<cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
        else:
            time +=1
            cache.remove(city)
            cache.append(city)
                    
    return time