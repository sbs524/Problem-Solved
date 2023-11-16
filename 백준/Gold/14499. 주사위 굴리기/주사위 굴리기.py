from collections import deque

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]
dice_mid = deque([0, 0, 0, 0])
dice_left = 0
dice_right = 0
for d in order:
    xx, yy = x + dxy[d-1][0], y + dxy[d-1][1]
    if not (0<=xx <n and 0<=yy<m):
        continue
    x, y = xx, yy
    if d==1:
        dice_right, dice_mid[0], dice_left, dice_mid[2] = dice_mid[2], dice_right, dice_mid[0], dice_left
    
    elif d==2:
        dice_right, dice_mid[0], dice_left, dice_mid[2] = dice_mid[0], dice_left, dice_mid[2], dice_right
        
    elif d==3:
        bottom = dice_mid.popleft()
        dice_mid.append(bottom)
    
    elif d==4:
        val = dice_mid.pop()
        dice_mid.appendleft(val)

    if maps[x][y]==0:
        maps[x][y] = dice_mid[0]
    else:
        dice_mid[0] = maps[x][y]
        maps[x][y] = 0
    print(dice_mid[2])