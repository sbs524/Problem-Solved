n = int(input())

arr = [[0]*15 for _ in range(15)]

for i in range(15):
    arr[i][1] = 1
    arr[0][i] = i
    

def find(k, n ):
    if arr[k][n]==0:
        arr[k][n] = find(k-1, n)+find(k, n-1)
    return arr[k][n]

for _ in range(n):
    k = int(input())
    n = int(input())
    print(find(k, n))