from collections import deque
ans = 0

n = int(input())
maps = [[0]*n for _ in range(n)]

k = int(input())
#사과 위치 입력
for _ in range(k):
    y, x = map(int, input().split())
    maps[y-1][x-1] = 2


dq = deque()
#시작위치
dq.append([0, 0])
maps[0][0] = 1
#0 : 동쪽, 1 : 남쪽....
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = 0

l = int(input())
dq2 = deque()
for i in range(l):
    cnt, dirt = input().split()
    cnt = int(cnt)
    if dirt == 'D':
        dq2.append([cnt, 1])
    elif dirt == 'L':
        dq2.append([cnt, -1])

while True:
    ans+=1
    cnt, direct = -1, 0
    if dq2:
        cnt, direct = dq2[0]
    y, x = dq[-1]
    y, x = y+dxy[direction][0], x+dxy[direction][1]
    # 꼬리거나 벽이면 종료
    if y<0 or y>=n or x<0 or x>=n or maps[y][x]==1:
        break

    #머리를 앞으로 전진
    dq.append([y, x])

    if ans==cnt:
        direction += direct
        dq2.popleft()
        if direction < 0:
            direction = 3
        elif direction >= 4:
            direction = 0

    #사과일 경우 꼬리는 그대로 냅둠
    if maps[y][x]==2:
        maps[y][x] = 1
        continue
    maps[y][x] = 1
    yy, xx = dq.popleft()
    maps[yy][xx]=0

print(ans)
