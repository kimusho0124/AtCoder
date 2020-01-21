
N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A))

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return(y)

def lcm(x, y):
    ans = (x * y) // gcd(x, y)
    return(ans)
l = 1
cnt = [0 for i in range(len(A))]
for i in range(len(A)):
    a = A[i]
    l = lcm(l, a)
    count = 0
    while True:
        if a % 2 == 0:
            a //= 2
            count += 1
        else:
            cnt[i] = count
            break
count = cnt[0]
flag = True
for i in range(len(A)):
    if cnt[i] != count:
        flag = False
        break
if flag:
    l = l // 2
    ans = M // l
    print((ans+1)//2)
else:
    print(0)