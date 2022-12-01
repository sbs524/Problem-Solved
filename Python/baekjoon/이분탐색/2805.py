answer=0
n, m=map(int, input().split())
trees=list(map(int, input().split()))
start, end=1, max(trees)
while start<=end:
    mid=(start+end)//2
    tree_len=0
    for tree in trees:
        if tree-mid>0:
            tree_len+=tree-mid
        
    if tree_len<m:
        end=mid-1
    elif tree_len>=m:
        answer=mid
        start=mid+1
print(answer)