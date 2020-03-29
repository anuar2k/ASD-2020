# Dana jest tablica n liczb A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.

# f(i, s) - czy z liczb a[1] od zera do a[i] da sie otrzymac sume s
# f(n, T)

# f(i, s) = f(i - 1, s) lub f(i-1, s-a[i]) pod warunkiem, ze s - a[i] > 0
# f(0, 0) - prawda
# f(0, s) - falsz dla s > 0

def subset(A, memo, i, s):
    if s == 0:
        return True
    if i < 0 or s < 0:
        return False

    if memo[i][s - 1] is not None:
        return memo[i][s - 1]

    if s - A[i] >= 0:
        memo[i][s - 1] = subset(A, memo, i - 1, s) or subset(A, memo, i - 1, s - A[i])
        return memo[i][s - 1]
    memo[i][s - 1] = subset(A, memo, i - 1, s)
    return memo[i][s - 1]

A = [1, 5, 2, 3, 8]
s = 19
memo = []
for i in range(len(A)):
    memo.append([])
    for j in range(s):
        memo[i].append(None)

print(subset(A, memo, len(A) - 1, s))
