N, K, S = map(int, input().split())
if S < 10 ** 9:
    A = [S if i < K else S+1 for i in range(N)]
else:
    A = [S if i < K else S-1 for i in range(N)]
print(*A)