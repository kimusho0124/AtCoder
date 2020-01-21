import math
X = int(input())
XX = 2 * X
data = [i for i in range(2,XX+1)]
limit = math.sqrt(XX)
prime = []
while True:
    p = data[0]
    if limit <= p:
        prime = prime + data
        break
    prime.append(p)
    data = [e for e in data if e % p != 0]
lenp = len(prime)
for i in range(lenp):
    if prime[i] >= X:
        print(prime[i])
        break