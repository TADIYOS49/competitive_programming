n, k = map(int,input().split())
joy = float('-inf')
for i in range(n):
    fi, ti = map(int,input().split())
    if k >= ti:
        joy = max(joy,fi)
    else:
        joy = max(joy,(fi-(ti-k)))
print(joy)