index=1
while True:
    l, p, v=map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    cnt=v//p
    print("Case "+str(index)+": "+str(l*cnt+min((v-(p*cnt)), l)))
    index+=1