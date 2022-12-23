def solution(s):
    answer = 0
    index, same, different=0, 0, 0
    
    for i in range(len(s)):
        if s[index]==s[i]:
            same+=1
        else:
            different+=1
            
        if same==different:
            answer+=1
            index=i+1
            same=0
            different=0
            
    if not(same==0 and different==0):
        answer+=1
    
    return answer