n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visits = [[0]*m for _ in range(n)]
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0

def find(locs, val, cnt):
    if cnt==4:
        global ans
        ans = max(ans, val)
        return
    
    for idx in range(4):
        for (y, x) in locs:
            yy = y + dxy[idx][0]
            xx = x + dxy[idx][1]
            if 0<=yy < n and 0 <= xx < m and visits[yy][xx]==0:
                visits[yy][xx]=1
                locs.append([yy, xx])
                find(locs, val + arr[yy][xx], cnt+1)
                visits[yy][xx]=0
                locs.pop()
                

for i in range(n):
    for j in range(m):
        locs = [[i, j]]
        visits[i][j]=1
        find(locs, arr[i][j], 1)
print(ans)