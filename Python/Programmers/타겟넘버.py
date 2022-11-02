def solution(numbers, target):
    answer = 0
    num_len=len(numbers)
    def dfs(index, val):
        if index==num_len:
            if val==target:
                nonlocal answer
                answer+=1
            return
        dfs(index+1, val+numbers[index])
        dfs(index+1, val-numbers[index])
    dfs(0,0)
    return answer