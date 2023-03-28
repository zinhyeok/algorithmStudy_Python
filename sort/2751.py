import sys

def ans():
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()

    for i in lst:
        print(i)

ans()