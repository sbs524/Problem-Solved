n = int(input())

arr = list(map(int, input().split()))
cnt = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            cnt[i] = max(cnt[i], cnt[j]+1)

print(max(cnt))