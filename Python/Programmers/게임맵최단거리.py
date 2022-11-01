from collections import deque

def solution(maps):
    answer = 0
    
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    
    
    dq=deque()
    dq.append([0, 0])
    
    len_mapx=len(maps[0])-1
    len_mapy=len(maps)-1
    
    visit=[[0]*(len_mapx+1) for i in range(len_mapy+1)]
    visit[0][0]=1 
    while dq:
        x, y=dq.popleft()
        for i in range(4):
            temp_x=x+dx[i]
            temp_y=y+dy[i]
            if temp_x<0 or temp_x>len_mapx or temp_y<0 or temp_y>len_mapy:
                continue
            if visit[temp_y][temp_x]==0 and maps[temp_y][temp_x]!=0:
                maps[temp_y][temp_x]=maps[y][x]+1
                dq.append([temp_x, temp_y])
                visit[temp_y][temp_x]=1
                
    print(maps)
    if maps[len_mapy][len_mapx]==1:
        return -1
    else:
        return maps[len_mapy][len_mapx]