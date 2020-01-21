from bisect import bisect_left
n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A_r = sorted(A, reverse = True)
cumsumA = [0]
total = 0
for i in range(n):
    total += A_r[i]
    cumsumA.append(total)

def func(x):
    ans = 0
    for i in range(n):
        kazu = x - A[i]
        idx = bisect_left(A, kazu)
        cou = n - idx
        ans += cou
    if ans >= m:
        return True
    else:
        return False

mi = 0
ma = 2 * 10 ** 5 + 1
while ma - mi > 1:
    mid = (mi + ma) // 2
    if func(mid):
        mi = mid
    else:
        ma = mid

ans = 0
count = 0

for ai in A_r:
    idx = bisect_left(A, mi - ai)
    ans += ai * (n - idx) + cumsumA[n - idx]
    count += n - idx
print(ans - (count-m) * mi)



