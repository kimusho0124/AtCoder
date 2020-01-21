N = int(input())
X = list(map(int, input().split()))
sosu = 10 ** 9 + 7
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

fac = [1 for i in range(N)]
inv = [0 for i in range(N)]
for i in range(1, N):
    fac[i] = fac[i-1] * i % sosu
    inv[i] = modinv(i, sosu)
#Sprint(fac)
ans = 0
for i in range(N):
    for j in range(i+1, N):
        kyori = X[j] - X[i]
        #print(kyori)
        if j == N-1:
            kaisu = fac[N-1] * inv[j-i] % sosu
            #(N-1)! / (j-i)#= (j-i-1)! * ((j-i-1)+ 1 + 1) * .. * (N-1)
        else:
            kaisu = (fac[N-1] * inv[j-i] % sosu) * inv[j-i+1] % sosu
            #(N-1)! / (j-i)(j-i+1) #(j-i-1)! * ((j-i-1) +2+1) * ... * (N-1)
        #print(kaisu)
        ans += kyori * kaisu % sosu
        ans = ans % sosu
print(ans)



'''
ma = X[N-1] - X[0]
S = [0 for i in range(N-1)]
for i in range(N-1):
    S[i] = X[i+1] - X[i]
kaijo = [1 for i in range(N)]
for i in range(1, N):
    kaijo[i] = kaijo[i-1] * i % sosu

print(S)
'''