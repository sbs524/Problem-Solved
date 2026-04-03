def solution(diffs, times, limit):
    answer, st, end = 300_000, 1, 300_000
    lens = len(diffs)
    
    while st <= end:
        level = (st + end) // 2
        score = 0

        # 점수계산
        for i in range(lens):
            if diffs[i] <= level:
                score += times[i]
            else:
                score += (times[i-1] + times[i]) * (diffs[i] - level) + times[i]

        if score <= limit:
            end = level - 1
            answer = level # 정답 갱신
        elif score > limit:
            st = level + 1
        
    return answer