import math, random

def lognEvenSort(A):
    even = [x for x in A if x % 2 == 0]
    even.sort()

    ptrA = 0
    ptrEven = 0
    ptrResult = 0
    result = []

    while ptrResult < len(A):
        if ptrA < len(A) and A[ptrA] % 2 == 0:
            ptrA += 1
        else:
            if ptrEven == len(even) or (ptrA != len(A) and A[ptrA] < even[ptrEven]):
                result.append(A[ptrA])
                ptrA += 1
            else:
                result.append(even[ptrEven])
                ptrEven += 1

            ptrResult += 1
    
    return result

n = 5
A = []

for _ in range(n ** 2):
    A.append(random.randrange(1, 100, 2))

A.sort()

for idx in random.sample(range(n ** 2), n):
    A[idx] = random.randrange(0, 100, 2)

print(A)
print(lognEvenSort(A))