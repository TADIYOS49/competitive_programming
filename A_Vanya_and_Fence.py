n,h = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
for i in arr:
    if i > h:
        count += 2
    else:
        count += 1
print(count)