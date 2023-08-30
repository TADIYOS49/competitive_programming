leng = int(input())
counter = 0
for i in range(leng):
    row = map(int,input().split())
    for item in row:
        if item == 1:
            counter += 1
print(counter//2)
