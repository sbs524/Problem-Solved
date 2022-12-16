def cal(arr):
    val=0
    while arr:
        imsi=arr.pop()
        if imsi=="+":
            val=arr.pop()+val
        elif imsi=="-":
            val=arr.pop()-val
        else:
            val=imsi
    return val

s=input()
arr=[]
index=0
for i in range(len(s)):
    if s[i]=="+":
        arr.append(int(s[index:i]))
        arr.append("+")
        index=i+1
    elif s[i]=="-":
        arr.append(int(s[index:i]))
        val=cal(arr)
        arr.clear()
        arr.append(val)
        arr.append("-")
        index=i+1
arr.append(int(s[index:]))
print(cal(arr))