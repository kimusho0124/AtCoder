N, K = map(int, input().split())
A = list(map(int, input().split()))
AA = [i % K for i in A]
print(AA)