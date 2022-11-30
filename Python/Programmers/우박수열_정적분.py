def solution(k, ranges):
    answer = []
    arr=[]
    while k>1:
        arr.append(k)
        if k%2==0:
            k=k//2
        else:
            k=k*3+1
    arr.append(1)
    area=[0]
    n=1
    for i in range(1, len(arr)):
        area.append((arr[i-1]+arr[i])/2)
        n+=1
    
    for i, j in ranges:
        j=n+j-1
        ans=0
        if i>j:
            answer.append(-1)
        else:
            for ii in range(i, j):
                ans+=area[ii+1]
            answer.append(ans)
        
        
        
        
    return answer