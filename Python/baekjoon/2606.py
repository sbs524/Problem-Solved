from collections import deque

n=int(input())
v=int(input())
graph=[[] for i in range(n+1)]
visit=[0]*(n+1)

for i in range(v):
    n1, n2=map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dq=deque()
dq.append(1)

while dq:
    computer=dq.popleft()
    visit[computer]=1
    for i in range(len(graph[computer])):
        if visit[graph[computer][i]]==0:
            visit[graph[computer][i]]=1
            dq.append(graph[computer][i])
            
print(sum(visit)-1)