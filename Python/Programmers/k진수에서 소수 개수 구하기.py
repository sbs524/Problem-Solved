def solution(n, k):
    answer = 0
    str_n=''    
    while n:
        str_n=str(n%k)+str_n
        n=n//k
    
    n_split=str_n.split('0')
    
    for num in n_split:
        if num=='':
            continue
        num_i=int(num)
        if num_i<2:
            continue
        elif num_i==2:
            answer+=1
        else:
            imsi=True
            for i in range(3, (int(num_i**0.5)+1)):
                if num_i%i==0:
                    imsi=False
                    break
            if imsi:
                answer+=1
            
    
    return answer