import math
sosu = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
g = A[0]
l = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
    l = l * A[i]
ans = 0
for i in range(N):
    ans += l // A[i]
    ans %= sosu
print(ans)