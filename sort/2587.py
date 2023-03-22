import sys

def ans():
    lst = []
    for i in range(5):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()
    avg = int(sum(lst)/len(lst))
    med = lst[2]
    print(avg)
    print(med)

ans()