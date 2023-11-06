n = int(input())

for i in range(n):
    arr = input()
    stack = []
    isTrue = True
    for j in range(len(arr)):
        if arr[j]=='(':
            stack.append(1)
        else:
            if len(stack)==0:
                isTrue = False
                break
            stack.pop()
    
    if isTrue and len(stack)==0:
        print("YES")
    else:
        print("NO")