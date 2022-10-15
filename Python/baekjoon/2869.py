a, b, v = map(int, input().split())

day = a-b
mok=v//day

ans=mok + 1 - (a//day)
distance = (mok*a)-((mok-1)*b)

while distance<v:
    distance+=day
    ans+=1 
    
print(ans)