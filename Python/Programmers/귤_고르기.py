def solution(k, tangerine):
    answer = 1
    fruit=[0]*10000000
    for fruits in tangerine:
        fruit[fruits-1]+=1
    fruit=sorted(fruit, reverse=True)
    ans=0
    for i in range(len(fruit)):
        if k-fruit[i]>0:
            k-=fruit[i]
            ans+=1
        elif k-fruit[i]<=0:
            answer=ans+1
            break
    
    return answer