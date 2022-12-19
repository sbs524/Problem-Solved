alphabet=['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

s=input()
cnt=len(s)
skip=0

for i in range(len(s)-1):
    if skip>0:
        skip-=1
        continue
    if s[i]=='c':
        if s[i+1]=='=' or s[i+1]=='-':
            cnt-=1
            skip=1
    elif s[i]=='d':
        if s[i+1]=='z':
            if i+2<len(s):
                if s[i+2]=='=':
                    cnt-=2
                    skip=2
        elif s[i+1]=='-':
            cnt-=1
            skip=1
        
        
    elif s[i]=='l' and s[i+1]=='j':
        cnt-=1
        skip=1
    
    elif s[i]=='n' and s[i+1]=='j':
        cnt-=1
        skip=1
    
    elif s[i]=='s' and s[i+1]=='=':
        cnt-=1
        skip=1
    
    elif s[i]=='z' and s[i+1]=='=':
        cnt-=1
        skip=1
    
print(cnt)