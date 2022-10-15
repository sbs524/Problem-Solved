def solution(nums):
    answer = 0
    pocketmon_dict={}
    for pocketmon in nums:
        pocketmon_dict[pocketmon]=pocketmon_dict.get(pocketmon, 0)+1
    
    if len(nums)//2<len(pocketmon_dict):
        answer=len(nums)//2
    else:
        answer = len(pocketmon_dict)
    
    return answer