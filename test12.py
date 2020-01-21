import math
N = int(input())
tax = 1.08
p0 = N / tax
p1 = (N+1) / tax
p = math.ceil(p0)
if p < p1:
    print(p)
else:
    print(':(')