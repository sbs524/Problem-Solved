from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]
ans = 0

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

dq = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j]==1:
            dq.append([i, j])
            
while dq:
    x, y = dq.popleft()
    for i in range(4):
        xx= dx[i]+x
        yy = dy[i]+y
        if 0<=xx and xx<m and 0<=yy and yy<n:
            if arr[xx][yy]==0:
                arr[xx][yy] = arr[x][y] + 1
                dq.append([xx, yy])

isTrue = False
for a in arr:
    for j in a:
        if j==0:
            ans = -1
            isTrue = True
            break
    if isTrue:
        break
    ans = max(max(a)-1, ans)
print(ans)