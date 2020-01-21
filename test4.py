sosu = 10 ** 9 + 7
X, Y = map(int, input().split())
amari = (X + Y) % 3
sho = (X + Y) // 3
x = 2 * sho - X
if amari == 0 and x >= 0 and x <= sho:
    fac = [1 for i in range(sho+1)]
    finv = [1 for i in range(sho+1)]
    inv = [1 for i in range(sho+1)]
    for i in range(2, sho+1):
        fac[i] = fac[i-1] * i % sosu
        inv[i] = sosu - inv[sosu%i] * (sosu//i) % sosu
        finv[i] = finv[i-1] * inv[i] % sosu
    #print(fac)
    #print(finv)
    ans = int(fac[sho] * (finv[x] * finv[sho-x] % sosu) % sosu)
else:
    ans = 0
print(ans)
