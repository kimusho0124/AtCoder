N = int(input())
A = list(map(int, input().split()))
sosu = 10 ** 9 + 7
dp = [0 for i in range(N)]
ans = 1
for i in range(N):
    if A[i] >= 1:
        nnn = dp[A[i]-1] - dp[A[i]]
    else:
        nnn = 3 - dp[A[i]]
    if nnn > 0:
        ans *= nnn
    elif nnn <= 0:
        ans *= 0
    ans = ans % sosu
    dp[A[i]] += 1
#print(dp)
print(ans)