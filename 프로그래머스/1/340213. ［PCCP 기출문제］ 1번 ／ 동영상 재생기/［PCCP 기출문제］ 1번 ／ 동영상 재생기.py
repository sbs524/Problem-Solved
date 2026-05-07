def to_second(time):
    mm, ss = map(int, time.split(":"))
    return mm * 60 + ss

def solution(video_len, pos, op_start, op_end, commands):
    video_sec = to_second(video_len)
    op_start_sec = to_second(op_start)
    op_end_sec = to_second(op_end)
    pos_sec = to_second(pos)
    
    def skip(cur_sec):
        if op_start_sec <= cur_sec < op_end_sec:
            return op_end_sec
        else:
            return cur_sec
                
    for command in commands:
        pos_sec = skip(pos_sec)
        
        if command == "next":
            pos_sec += 10
        elif command == "prev":
            pos_sec -=10
        
        if pos_sec < 0:
            pos_sec = 0
        elif video_sec < pos_sec:
            pos_sec = video_sec
        
        pos_sec = skip(pos_sec)
    
    mm = pos_sec // 60
    ss = pos_sec % 60
    answer = f"{mm:02d}:{ss:02d}"
    return answer
