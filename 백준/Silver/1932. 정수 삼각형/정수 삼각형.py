n = int(input())

arr = [0]*n

for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(1, n):
    arr[i][0] += arr[i-1][0]
    arr[i][i] += arr[i-1][i-1]
    
    for j in range(1, i):
        arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])

print(max(arr[n-1]))