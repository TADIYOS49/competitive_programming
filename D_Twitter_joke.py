n = int(input())
reposts = {}
reposts['polycarp'] = 1
for _ in range(n):
    name1, _, name2 = input().split()
    reposts[name1.lower()] = reposts[name2.lower()]+1
print(max(reposts.values()))