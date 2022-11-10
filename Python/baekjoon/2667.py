from collections import deque

n=int(input())
visit=[[0]*n for i in range(n)]
graph=[]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
dq=deque()

ans=[]

for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and graph[i][j]==1:
            dq.append([i, j])
            cnt=0
            while dq:
                y, x=dq.popleft()
                visit[y][x]=1
                cnt+=1
                for k in range(4):
                    xx=x+dx[k]
                    yy=y+dy[k]
                    if xx>=n or xx<0 or yy>=n or yy<0:
                        continue
                    if visit[yy][xx]==0 and graph[yy][xx]==1:
                        dq.append([yy, xx])
            ans.append(cnt)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])                        