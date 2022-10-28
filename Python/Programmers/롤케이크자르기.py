def solution(topping):
    answer = 0
    cake_after={}
    for i in topping:
        cake_after[i]=cake_after.get(i, 0)+1
        
    cake_before={}
    
    for i in topping:
        cake_before[i]=1
        cake_after[i]-=1
        if cake_after[i]==0:
            del cake_after[i]
        if len(cake_before)==len(cake_after):
            answer+=1
            
    
    return answer