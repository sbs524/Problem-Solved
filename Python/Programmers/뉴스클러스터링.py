def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    intersaction = []
    sumSet = []
    
    for i in range(len(str1)-1):
        if (str1[i] >= 'a' and str1[i]<='z') and (str1[i+1] >= 'a' and str1[i+1]<='z'):
            intersaction.append(str1[i:i+2])
        
    for i in range(len(str2)-1):
        if (str2[i] >= 'a' and str2[i]<='z') and (str2[i+1] >= 'a' and str2[i+1]<='z'):
            sumSet.append(str2[i:i+2])
    
    cnt = 0
    
    visit_s=[0 for i in range(len(sumSet))]
    visit_i=[0 for i in range(len(intersaction))]
    
    if len(intersaction)<len(sumSet):
        for i in range(len(intersaction)):
            for j in range(len(sumSet)):
                if visit_s[j]:
                    continue
                if intersaction[i]==sumSet[j]:
                    visit_s[j] = 1
                    visit_i[i] = 1
                    cnt+=1
                    break
                    
    else:
        for i in range(len(sumSet)):
            for j in range(len(intersaction)):
                if visit_i[j]:
                    continue
                if sumSet[i]==intersaction[j]:
                    visit_i[j] = 1
                    visit_s[i] = 1
                    cnt+=1
                    break
                    
    sum_cnt = cnt
    for i in range(len(visit_s)):
        if visit_s[i]==0:
            sum_cnt+=1
    for i in range(len(visit_i)):
        if visit_i[i]==0:
            sum_cnt+=1
    
    print(intersaction, sumSet)
    if sum_cnt==0:
        return 65536
    return int((cnt/sum_cnt)*65536)