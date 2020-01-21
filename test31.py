N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

sosu = 10 ** 9 + 7
fac = [1 for i in range(N)]
finv = [1 for i in range(N)]
inv = [1 for i in range(N)]
for i in range(2, N):
    fac[i] = fac[i-1] * i % sosu
    inv[i] = sosu - inv[sosu%i] * (sosu // i) % sosu
    finv[i] = finv[i-1] * inv[i] % sosu
ans = 0

for i in range(N-K+1):
    ans += (((((A[-i-1] - A[i]) * fac[N-1-i]) % sosu ) * finv[K-1]) % sosu ) * finv[N-i-K] % sosu
    ans = ans % sosu
print(ans)
