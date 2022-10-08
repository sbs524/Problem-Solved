from collections import deque

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        dq=deque()
        done = True
        for j in range(len(s)):
            if s[j]=='[' or s[j]=='{' or s[j]=='(':
                dq.append(s[j])
            else:
                if dq:
                    char=dq.pop()
                    if (char=='['and s[j]==']'):
                        continue
                    elif (char=='{' and s[j]=='}'):
                        continue
                    elif (char=='(' and s[j]==')'):
                        continue   
                done=False
                break             
        if done and not dq:
            answer+=1
        s = s[1:]+s[0]
        
    return answer