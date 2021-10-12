def solution(cacheSize, data):
    cities=[]
    for i in range(len(data)):
        cities.append(data[i].lower())
    answer = 0
    cache = []
    if cacheSize==0:
        return len(cities)*5
    for ref in cities:
        if ref not in cache:
            answer+=5
            if len(cache) < cacheSize:
                cache.append(ref)
            else:
                cache.pop(0)
                cache.append(ref)
        else:
            cache.pop(cache.index(ref))
            cache.append(ref)
            answer+=1
    return answer

# LRU 알고리즘