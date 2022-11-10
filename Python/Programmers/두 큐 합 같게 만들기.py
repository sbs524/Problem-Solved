from collections import deque

def solution(queue1, queue2):
    answer = 0
        
    queue_sum=sum(queue1)+sum(queue2)
    if queue_sum%2==0:
        queue_sum=queue_sum//2
        q1=deque(queue1)
        q2=deque(queue2)
        queue_len=(len(queue1)+len(queue2))*2
        q1_sum=sum(queue1)
        q2_sum=sum(queue2)
        
        while True:
            if q1_sum>queue_sum:
                val=q1.popleft()
                q2.append(val)
                q1_sum-=val
                q2_sum+=val
                answer+=1
                
            elif q2_sum>queue_sum:
                val=q2.popleft()
                q1.append(val)
                q2_sum-=val
                q1_sum+=val
                answer+=1
            else:
                break
            if answer==queue_len:
                answer=-1
                break
    
    else:
        return -1
    
    
    return answer