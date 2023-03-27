import sys

def ans():
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = sys.stdin.readline().strip().split()
        lst.append([int(a),b])
    lst.sort(key= lambda x:x[0])

    for i in lst:
        print(i[0], end=" ")
        print(i[1])
        

ans()