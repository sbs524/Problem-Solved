
def solution(n, times):
    end=n*min(times)
    start=1
    cnt=0
    mid=0
    
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for time in times:
            cnt+=mid//time
        
        if cnt==n:
            break
        if cnt<n:
            start=mid+1
        elif cnt>n:
            end=mid-1
    
    if cnt<n:
        mid+=1
    
    while mid>0:
        mid-=1
        cnt=0
        for time in times:
            cnt+=mid//time
        if cnt<n:
            mid+=1
            break
    
    
    return mid