def solution(genres, plays):
    info = {}
    plays_genres = []
    ans = []
    for i in range(len(genres)):
        if genres[i] in info.keys():
            info[genres[i]] += plays[i]
        else:
            info[genres[i]] = plays[i]

    for i in info.keys():
        plays_genres.append([i, info[i]])

    plays_genres.sort(key=lambda x: x[1], reverse=True)
    for i in plays_genres:
        candidate = []
        for j in range(len(genres)):
            if i[0] == genres[j]:
                candidate.append([plays[j], plays.index(plays[j])])
                plays[j]=-1
        candidate.sort(key=lambda x: (-x[0], x[1]))
        ans.append(candidate[0][1])
        if len(candidate) > 1:
            ans.append(candidate[1][1])

    return ans

# dict 자료형 sort