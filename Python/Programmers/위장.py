def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for clothe, type in clothes:
        clothes_dict[type] = clothes_dict.get(type, 0)+1
    
    
    for i in clothes_dict:
        answer*=(clothes_dict[i]+1)
            
    return answer - 1