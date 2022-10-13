def solution(n, left, right):
    arr=[0 for i in range(n*((right//n)-(left//n)+1))]
    index=left//n+1
    arr_index=(index-1)*n
    idx=0
    
    while arr_index<=right:
        cnt=index
        while cnt!=0:
            arr[idx]=index
            cnt-=1
            arr_index+=1
            idx+=1
            
        cnt=index
        for i in range(n-index):
            cnt+=1
            arr[idx]=cnt
            arr_index+=1
            idx+=1
        index+=1
        
    return arr[left%n:right-left+(left%n)+1]