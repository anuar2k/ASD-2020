# Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2))

# 1 7 2 5 8
# 0 1 8 2 8

# wynik: 1 2 8

# F(n, m) - długość najdłuższego wspólnego podciągu ciągów A[1..n] i B[1..n]
# F(n, m) = F(n-1, m-1) + 1, jeśli A[n] = B[m]
# F(n, m) = max(F(n, m-1), F(n-1, m)), jeśli A[n] 1= B[m]
# F(n, 0) = 0
# F(0, m) = 0

def NWP(A, B):
    n = len(A)
    m = len(B)
    C = [None] * (n + 1)
    for i in range(n + 1):
        C[i] = [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range (1, m + 1):
            if A[i - 1] == B[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i - 1][j], C[i][j - 1])
    return C[n][m]

A=[1, 2, 5, 8, 2]
B=[2, 5, 7, 11, 2, 8]
print(NWP(A, B))