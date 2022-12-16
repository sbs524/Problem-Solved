k, n=map(int, input().split())
arr=[]
answer=0
for i in range(k):
    arr.append(int(input()))
start=1
end=min(arr)
while start<=end:
    mid=(start+end)//2
    cnt=0
    for lan in arr:
        cnt+=lan//mid
    if cnt<n:
        end=mid-1
    else:
        answer=mid
        start=mid+1
print(answer)