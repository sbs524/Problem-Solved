n=int(input())
for i in range(n):
    cnt=int(input())
    arr=[0]*cnt
    for j in range(cnt):
        arr[j]=list(map(int, input().split()))
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