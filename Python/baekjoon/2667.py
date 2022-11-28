n=int(input())

arr=[]
ans=[]

for i in range(n):
    arr.append(list(map(int, input())))
visits=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visits[i][j]==0:
            if arr[i][j]==0:
                visits[i][j]=1
                continue
            cnt=0
            stack=[[i, j]]
            while stack:
                y, x=stack.pop()
                if y<0 or y>=n or x<0 or x>=n:
                    continue
                if visits[y][x]==1:
                    continue
                visits[y][x]=1
                if arr[y][x]==1:
                    cnt+=1
                    stack.append([y+1, x])
                    stack.append([y-1, x])
                    stack.append([y, x+1])
                    stack.append([y, x-1])
            ans.append(cnt)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])