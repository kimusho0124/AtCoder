import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

J = [i for i in range(1, N+1)]
JJ = list(itertools.permutations(J))
for i in range(len(JJ)):
    if P == JJ[i]:
        pp = i
    if Q == JJ[i]:
        qq = i
print(abs(pp - qq))