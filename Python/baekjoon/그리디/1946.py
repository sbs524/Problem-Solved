import sys
input=sys.stdin.readline

n=int(input())
for i in range(n):
    cnt=int(input())
    arr=[list(map(int, input().split())) for _ in range(cnt)]
    arr=sorted(arr, key=lambda x:x[0])
    
    ans=1
    rang=arr[0][1]
    for j in range(1, cnt):
        if rang>arr[j][1]:
            ans+=1
            rang=arr[j][1]
        if rang==1:
            break
        
    print(ans)