n = input()
p = []
while True:
    try:
        temp = int(input())
        p.append(temp)
    except EOFError:
        break
collect = {}
for i in p:
    if i in collect:
        collect[i] += 1
    else:
        collect[i] = 1
print(len(collect))