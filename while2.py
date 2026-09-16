N = int(input())
K = int(input())
Q = 0
while N >= K:
    N -= K
    Q += 1
print(Q, N)
