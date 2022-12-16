n=int(input())
road=list(map(int, input().split()))
price=list(map(int, input().split()))

min_price=min(price[:-1])
answer=0
current=0

for i in range(len(price)-1):
    if price[i]==min_price:
        left_road=0
        for j in range(current, i):
            left_road+=road[j]            
        answer+=price[current]*left_road
        current=i
        
        left_road=0
        for j in range(current, len(road)):
            left_road+=road[j]
        answer+=price[i]*left_road
        break
    
    elif price[i]>price[i+1] or i==n-2:
        left_road=0
        for j in range(current, i+1):
            left_road+=road[j]            
        answer+=price[current]*left_road
        current=i+1
        
        
    
print(answer)