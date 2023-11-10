n, m = map(int, input().split())
r, c, d = map(int, input().split())
forward = [[-1, 0], [0, 1], [1, 0], [0, -1]]
back = [[1, 0], [0, -1], [-1, 0], [0, 1]]

arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    if arr[r][c]==0:
        ans+=1
        arr[r][c]=2
    # 주위 4칸 중 청소하지 않은 칸이 있는지 체크
    isTrue = True
    for i in range(4):
        dy = r+forward[i][0]
        dx = c+forward[i][1]
        if 0<=dy<n and 0<=dx<m and arr[dy][dx]==0:
            isTrue = False
            break

    #4칸 모두 청소하지 않은 경우
    if isTrue:
        dy = r + back[d][0]
        dx = c + back[d][1]
        if 0<=dy<n and 0<= dx < m and (arr[dy][dx]==0 or arr[dy][dx]==2):
            r, c = dy, dx
            continue
        break
    
    d-=1
    if d < 0:
        d = 3
    dy, dx = r+forward[d][0], c+forward[d][1]
    if 0<=dy<n and 0<=dx<m and arr[dy][dx]==0:
        r, c = dy, dx
        
print(ans)