N, M = map(int, input().split())
WAC = [0 for i in range(N)]
TF = [0 for i in range(N)]
for i in range(M):
    p, S = input().split()
    p = int(p)-1
    if S == 'AC':
        TF[p] = 1
    if TF[p] == 0 and S == 'WA':
        WAC[p] += 1
count = 0
for i in range(N):
    count += TF[i] * WAC[i]
print(sum(TF), count)

