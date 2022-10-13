from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque()
    for i in range(len(progresses)):
        dq.append(progresses[i])
    
    cnt=0
    while dq:
        if dq[0]>=100:
            dq.popleft()
            speeds=speeds[1:]
            cnt+=1
            continue
        for i in range(len(dq)):
            dq[i]+=speeds[i]
        if cnt>0:
            answer.append(cnt)
            cnt=0
    if cnt>0:
        answer.append(cnt)
    return answer