a=int(input())
while a>0:
    n=int(input())
    arr=[int(i) for i in input().split()]
    nOne=arr.count(-1)
    one=arr.count(1)
    ans=0
    while True:
        if one>=nOne:
            if nOne%2==0:
                print(ans)
                break
            else:
                ans+=1
                nOne-=1
        else:
            ans+=1
            one+=1
            nOne-=1
  
    a-=1