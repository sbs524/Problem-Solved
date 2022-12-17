n=int(input())
arr=[int(input()) for _ in range(n)]
arr.sort(reverse=True)
ans=[]
for i in range(n):
    ans.append(arr[i]*(i+1))
print(max(ans))