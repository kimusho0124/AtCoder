A, B, K = map(int, input().split())
if A >= K:
    print(A-K, end = ' ')
    print(B)
elif A < K and A+B >= K:
    print(0, end = ' ')
    print(A+B-K)
else:
    print('0 0')