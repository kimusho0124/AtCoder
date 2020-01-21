import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
lenL = len(L)
ans = 0
for i in range(lenL-2):
    for j in range(i+1, lenL-1):
        a = L[i]
        b = L[j]
        ind = bisect.bisect_left(L[j+1:], a+b)
        ans += ind
print(ans)

