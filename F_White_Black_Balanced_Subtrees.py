from collections import defaultdict

def count_balanced_subtrees(n, parents, colors):
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
    count = 0
    def dfs(node):
        nonlocal count
        white, black = 0, 0
        for child in tree[node]:
            w, b = dfs(child)
            white += w
            black += b
        if colors[node - 1] == 'W':
            white += 1
        else:
            black += 1
        if white == black:
            count += 1
        return white, black
    dfs(1)
    return count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        parents = list(map(int, input().split()))
        colors = input()
        print(count_balanced_subtrees(n, parents, colors))

import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start(); thread.join()