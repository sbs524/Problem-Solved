n = int(input())

arr = list(map(int, input().split()))
cnt_list = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            cnt_list[i] = max(cnt_list[i], cnt_list[j]+1)
            
for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            cnt_list[i] = max(cnt_list[i], cnt_list[j]+1)
            
print(max(cnt_list))