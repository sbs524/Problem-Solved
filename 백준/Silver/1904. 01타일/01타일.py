n = int(input())

if n==1:
    print(1)
elif n==2:
    print(2)
else:
    first = 1
    second = 2

    for i in range(3, n+1):
        val = first + second
        first = second
        second = val%15746

    print(second%15746)