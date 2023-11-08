from collections import deque
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

def dfs(arr):
    visit = copy.deepcopy(arr)
    dq = deque()
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 2:
                dq.append([i, j])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0<=yy<n and 0<=xx<m and visit[yy][xx]==0:
                visit[yy][xx]=2
                dq.append([yy, xx])
    cnt=0
    for v in visit:
        cnt += v.count(0)
    return cnt


def select(arr, idx):
    if idx==3:
        global ans
        ans = max(dfs(arr), ans)
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][j] = 1
                select(arr, idx+1)
                arr[i][j] = 0
        
    
select(arr, 0)
print(ans)