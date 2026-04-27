def solution(players, m, k):
    answer = 0
    for i in range(24):
        if m <= players[i]:
            serverCnt =players[i] // m
            answer += serverCnt
            for j in range(i, i+k):
                if j >= 24:
                    break
                players[j] -= m * serverCnt
    return answer