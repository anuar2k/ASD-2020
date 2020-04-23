import math, random

def SumSort(A, B):
    n = math.isqrt(len(A))
    sums = []
    for i in range(n):
        currSum = 0
        for j in range(i * n, (i + 1) * n):
            currSum += A[j]
        sums.append((i, currSum))

    sums = sorted(sums, key=lambda x: x[1])
    for i in range(n):
        for j in range(n):
            B[i * n + j] = A[sums[i][0] * n + j]

    print([x[1] for x in sums])

n = 7
A = [random.randint(0, 49) for _ in range(n ** 2)]

B = [None] * len(A)

SumSort(A, B)

print(B)
