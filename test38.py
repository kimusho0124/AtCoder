N = int(input())
P = list(map(int, input().split()))
nm = P[0]
count = 0
for i in range(N):
    if P[i] <= nm:
        count += 1
        nm = P[i]
print(count)
