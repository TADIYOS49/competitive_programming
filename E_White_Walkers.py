import sys, threading

input = lambda: sys.stdin.readline().strip()

def solve(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return solve(n//2)+solve(n%2)+solve(n//2)

def main():
    print(3%2)
    num , left, right = map(int, input().split())
    ans = [solve(num)]
    count = 0
    left -= 1
    right -= 1
    while left <= right:
        if ans[left] == 1:
            count+=1
    print(count)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()