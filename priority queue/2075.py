import sys
N = int(input())
lst = []
#메모리 제한
for i in range(N):
    lst = lst + list(map(int,sys.stdin.readline().strip().split()))
    lst.sort(reverse=True)
    lst = lst[0:N]

print(lst[N-1])