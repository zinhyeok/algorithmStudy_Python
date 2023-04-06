N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

def combination(arr, r):
    want = []
    if r==1:
        for i in arr:
            want.append([i])
    else:
        for i in range(len(arr)-r+1):
            for j in combination(arr[i+1:], r-1):
                want.append([arr[i]]+j)
    return want

for _ in combination(lst,3):
    if M >= sum(_) and (M-ans)>(M-sum(_)):
        ans = sum(_)
        ans_lst = _
    else:
        pass
print(ans)