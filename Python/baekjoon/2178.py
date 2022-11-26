from collections import deque

n, m=map(int, input().split())
arr=[]
for i in range(n):
    s=input()
    arr.append([int(char) for char in s])
dq=deque()

dq.append([0, 0])
visits=[[0]*m for _ in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

while dq:
    y, x = dq.popleft()
    visits[y][x]=1
    if y==n-1 and x==m-1:
        break
    for i in range(4):
        dyy=dy[i]+y
        dxx=dx[i]+x
        if 0>dyy or n<=dyy or 0>dxx or m<=dxx:
            continue
        if visits[dyy][dxx]==0 and arr[dyy][dxx]==1:
            dq.append([dyy, dxx])
            arr[dyy][dxx]=arr[y][x]+1
print(arr[n-1][m-1])