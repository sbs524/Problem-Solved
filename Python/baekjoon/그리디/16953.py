a, b=map(int, input().split())
cnt=1
while a<b:
    if b%2==0:
        b=b//2
    elif b%10==1:
        b=b//10
    else:
        break
    cnt+=1
if a==b:
    print(cnt)
else:
    print(-1)