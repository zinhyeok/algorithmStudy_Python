

def ans():
    N = str(input())
    lst = [x for x in N]
    lst.sort(reverse=True)

    for i in lst:
        print(i, end="")


ans()