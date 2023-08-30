t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    arr.sort()
    i=0
    j=n-1
    sumlast=0
    sumfirst=0
    canHappen=False
    while i<=j:
        if n-j<i+1 and sumlast>sumfirst:
            canHappen=True
            break
        elif j>=0 and sumlast<=sumfirst:
            sumlast+=arr[j]
            j-=1
        else:
            sumfirst+=arr[i]
            i+=1
    if n-j<i+1 and sumlast>sumfirst:
        canHappen=True
    # print(sumlast)
    # print(sumfirst)
    if canHappen:
        print('YES')
    else:
        print('NO')