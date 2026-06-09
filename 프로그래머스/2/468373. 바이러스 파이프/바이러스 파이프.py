from collections import deque

def solution(n, infection, edges, k):
    answer = 1
    node_graph = [[[] for _ in range(n + 1)] for _ in range(4)]
    
    for x, y, pipe_type in edges:
        # 양방향 저장
        node_graph[pipe_type][x].append(y)
        node_graph[pipe_type][y].append(x)
    
    # 감염수행
    def spread(infected, pipe_type):
        dq = deque(infected)
        visited = set(infected)
        
        while dq:
            cur = dq.popleft()
            for nx in node_graph[pipe_type][cur]:
                if nx not in visited:
                    dq.append(nx)
                    visited.add(nx)
                    infected.add(nx)
            
        
    def dfs(depth, infected):
        nonlocal answer
        
        answer = max(answer, len(infected))
        
        if depth == k:
            return
        
        for i in range(1, 4):
            next_infected = infected.copy()
            spread(next_infected, i)
            dfs(depth + 1, next_infected)
    
    dfs(0, {infection})
    
    return answer