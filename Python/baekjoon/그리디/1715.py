from heapq import heappush, heappop
n=int(input())
arr=[]
cnt=0
for i in range(n):
    heappush(arr, int(input()))
while len(arr)>1:
    s=heappop(arr)+heappop(arr)
    cnt+=s
    heappush(arr, s)

print(cnt)