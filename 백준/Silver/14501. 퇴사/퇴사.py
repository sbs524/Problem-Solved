n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cost = [0]*(n+1)
ans=0

for i in range(n):
    day = i + arr[i][0]
    if day>n:
        continue
    val = max(cost[:i+1])
    val += arr[i][1]
    cost[day] = max(val, cost[day])
print(max(cost))
