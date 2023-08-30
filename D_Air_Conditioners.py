q = int(input())

def solve(kmap,n):
    left = []
    prevmin = float('inf')
    for i in range(n):
        if i in kmap:
            left.append(min(kmap[i],prevmin+1))
            prevmin = min(kmap[i],prevmin+1)
        else:
            left.append(prevmin+1)
            prevmin += 1
    right = [0] * n
    prevmin = float('inf')
    for i in range(n)[::-1]:
        if i in kmap:
            right[i] = min(kmap[i],prevmin+1)
            prevmin = min(kmap[i],prevmin+1)
        else:
            right[i] = prevmin+1
            prevmin += 1
    ans = [0] * n
    for i in range(len(left)):
        ans[i] = min(left[i],right[i])
    print(*ans)

        

for _ in range(q):
    __ = input()
    n,k = map(int,input().split())
    karr = list(map(int,input().split()))
    ktemp = list(map(int,input().split()))
    kmap = {}
    for i in range(len(karr)):
        kmap[karr[i]-1] = ktemp[i]
    solve(kmap,n)

