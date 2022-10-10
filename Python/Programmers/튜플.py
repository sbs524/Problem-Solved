def solution(s):
    answer=[]
    visit=[0 for i in range(len(s.split('}')))]
    s=s[2:-2].split('},{')
    cnt=1
    for i in range(len(s)):
        for j in range(len(s)):
            if visit[j]:
                continue
            int_arr=list(map(int, s[j].split(',')))
            if cnt==len(int_arr):
                visit[j]=1
                for k in range(len(answer)):
                    int_arr.remove(answer[k])
                answer+=int_arr   
        cnt+=1
        
        
    return answer