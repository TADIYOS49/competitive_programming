from collections import defaultdict
n = int(input())
string = input().lower()
dic = defaultdict(int)

for i in range(n):
    dic[string[i]] += 1

if len(dic) < 26:
    print("NO")
else:
    print("YES")