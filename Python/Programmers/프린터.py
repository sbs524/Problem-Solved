from collections import deque

def solution(priorities, location):
    answer = 1
    dq=deque()
    
    for priority in priorities:
        dq.append(priority)
    
    while dq:
        priority = dq.popleft()
        istrue=False
        for i in dq:
            if priority<i:
                istrue=True
                break
        
        if istrue:
            dq.append(priority)
            location-=1
            if location<0:
                location=len(dq) - 1
        
        else:
            if location==0:
                break
            answer+=1
            location-=1
            if location<0:
                location=len(dq) - 1
            
    
    
    return answer