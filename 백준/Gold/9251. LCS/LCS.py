s1 = input()
s2 = input()

len1, len2 = len(s1)+1, len(s2)+1

cnt = [[0]*(len2) for _ in range(len1)]
ans = 0

for i in range(1, len1):
    for j in range(1, len2):
        if s1[i-1]==s2[j-1]:
            cnt[i][j] = max(cnt[i-1][j-1]+1, cnt[i-1][j], cnt[i][j-1])
        else:
            cnt[i][j] = max(cnt[i-1][j], cnt[i][j-1])
    ans = max(ans, max(cnt[i]))
print(ans)