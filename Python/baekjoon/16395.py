n, k=map(int, input().split())
arr=[]
for i in range(n):
    arr.append([])
    for j in range(i+1):
        if j==0 or j==i:
            arr[i].append(1)
        else:
            arr[i].append(arr[i-1][j-1]+arr[i-1][j])
print(arr[n-1][k-1])