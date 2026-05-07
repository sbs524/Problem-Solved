def solution(video_len, pos, op_start, op_end, commands):
    video_mm, video_ss = map(int, video_len.split(":"))
    start_mm, start_ss = map(int, op_start.split(":"))
    end_mm, end_ss = map(int, op_end.split(":"))
    
    start_cnt = start_mm * 60 + start_ss
    end_cnt = end_mm * 60 + end_ss
    
    def skip(cur):
        mm, ss = map(int, cur.split(":"))
        cur_cnt = mm * 60 + ss
        
        if start_cnt <= cur_cnt and cur_cnt < end_cnt:
            return op_end
        else:
            return cur
                
    for command in commands:
        pos = skip(pos)
        mm, ss = map(int, pos.split(":"))
        
        if command == "next":
            ss += 10
        elif command == "prev":
            ss -=10
        
        if 60 < ss:
            ss -=60
            mm += 1
        elif ss < 0:
            ss +=60
            mm -=1
        
        if mm < 0:
            mm, ss = 0, 0
        elif video_mm <= mm and video_ss < ss:
            mm, ss = video_mm, video_ss
        
        pos = f"{mm:02d}:{ss:02d}"
        pos = skip(pos)
        
    return pos
