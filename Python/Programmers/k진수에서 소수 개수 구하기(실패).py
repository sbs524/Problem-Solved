def solution(n, k):
    answer = 0
    numbers=[]
    num_str=''
    
    while n:
        num_str=str(n%k) +num_str
        n=n//k
    
    start=0
    end=0
    for i in range(len(num_str)):
        print(start, end)
        if num_str[i]=='0':
            if start<end:
                numbers.append(int(num_str[start:end]))
                start=i+1
                end=i+1
            else:
                start=i+1
                end=i+1
        else:
            end+=1
    if start<end:
        numbers.append(int(num_str[start:end]))
        
    num_max=max(numbers)
    prime_num=[True]*(num_max+1)
    prime_num[0]=False
    prime_num[1]=False
    index=2
    while index<=num_max:
        if prime_num[index]==True:
            imsi=index+index
            while imsi<=num_max:
                prime_num[imsi]=False
                imsi+=index
        index+=1
    
    for i in numbers:
        if prime_num[i]==True:
            answer+=1
    
    return answer