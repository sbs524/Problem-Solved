def solution(n, computers):
    answer = 0
    visited = [0] * n
                
    def dfs(n):
        nonlocal visited
        
        if visited[n] == 1:
            return
        
        # 방문처리
        visited[n] = 1
        
        for i in range(len(computers[n])):
            if computers[n][i] == 1:
                dfs(i)
    
    for i in range(len(computers)):
        # 방문하지 않은 노드일때만 수행
        if visited[i] == 0:
            answer += 1
            dfs(i)
    
    return answer