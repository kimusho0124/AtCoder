import math
N = int(input())
x = [0 for i in range(N)]
y = [0 for i in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())
kaijo = 1
for i in range(1,N+1):
    kaijo *= i
kaisu = kaijo * (N-1)
hen = N * (N-1) // 2
wa = 0
for i in range(N):
    for j in range(i+1,N):
        kyori = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        wa += kyori * kaisu / hen
print(wa / kaijo)