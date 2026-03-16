def solution(dirs):
    answer = 0
    LEN= 5
    MAP_LEN = LEN * 2 + 1
    dir_map = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }
    vector_map = {
        "U": "D",
        "D": "U",
        "R": "L",
        "L": "R"
    }
    game_map = [[{"U" : 0, "D" : 0, "R" : 0, "L" : 0} for _ in range(MAP_LEN)] for _ in range(MAP_LEN)]
    x, y = LEN, LEN
    print(game_map)
    
    # 입력받은_경로대로_이동
    for next_dir in dirs:
        dx, dy = dir_map[next_dir]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx and nx < MAP_LEN and 0 <= ny and ny < MAP_LEN:
            # 해당_경로_방문_유무_체크
            if game_map[y][x][next_dir] == 0:
                answer += 1
                game_map[y][x][next_dir] = 1
                game_map[ny][nx][vector_map[next_dir]] = 1
            x, y = nx, ny

    return answer