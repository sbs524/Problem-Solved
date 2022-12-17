s=input()
cnt=0
a='2'
for i in range(len(s)):
    if a!=s[i]:
        cnt+=1
        a=s[i]
print(cnt//2)