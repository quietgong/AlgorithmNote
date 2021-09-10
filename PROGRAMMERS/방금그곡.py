def playing_time(start_time, finish_time):
    finish_time = finish_time.split(":")
    start_time = start_time.split(":")
    play_time = (int(finish_time[0]) * 60 + int(finish_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))
    return play_time

def solution(m, musicinfos):
    answer = []
    change = [['C#', 'c'], ['D#', 'd'], ['F#', 'f'], ['G#', 'g'], ['A#', 'a']]
    for i in range(len(change)):
        m = m.replace(change[i][0], change[i][1])

    for musicinfo in musicinfos:
        playing_melody = ''
        info = musicinfo.split(",")
        start_time = info[0]
        finish_time = info[1]
        song_name = info[2]
        melody = info[3]

        for i in range(len(change)):
            melody = melody.replace(change[i][0], change[i][1])

        play_time = playing_time(start_time,finish_time)

        for i in range(play_time):
            i %= len(melody)
            playing_melody += melody[i]
        if m in playing_melody:
            answer.append((song_name, play_time))

    if len(answer) == 0:
        return "(None)"
    else:
        answer.sort(key=lambda x: x[1], reverse=True)
        return answer[0][0]

# 문제를 제대로 이해한 뒤 푼다, C와 C#을 다르게 인식하기 위해 C#을 한글자의 단어로 치환시키는 테크닉
# 충족하는 조건이 여러 경우인 경우 출력하는 방법