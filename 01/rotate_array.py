# algorytmy obrotu tablicy o k pozycji w czasie O(n) (vs. naiwne O(nk))

from math import gcd

#-------------------------------------------

def ceil_div(a, b):
    return (a // b) + (a % b != 0)

def mirror(arr, l, r):
    for offset in range(ceil_div(r - l, 2)):
        arr[l + offset], arr[r - offset] = arr[r - offset], arr[l + offset]

# obrót przez lustrzane odbicia
def rotateMirror(arr, k):
    n = len(arr)
    k = k % n

    mirror(arr, 0    , n - k - 1)
    mirror(arr, n - k, n     - 1)
    mirror(arr, 0    , n     - 1)

    return arr

#-------------------------------------------

def jumpCycle(arr, start, k):
    pos = start
    carry = arr[start]
    jumpCnt = 0
    n = len(arr)
    cycle = True
    while(cycle):
        pos = (pos + k) % n
        arr[pos], carry = carry, arr[pos]
        cycle = pos != start
        jumpCnt = jumpCnt + 1
    return jumpCnt
    
# obrót przez skoki o n pozycji, bez nwd
def rotateJump(arr, k):
    n = len(arr)
    jumpCnt = 0
    pos = 0
    while (jumpCnt < n):
        jumpCnt = jumpCnt + jumpCycle(arr, pos, k)
        pos = pos + 1
    return arr

#-------------------------------------------

def jumpCycleGCD(arr, start, k):
    pos = start
    carry = arr[start]
    n = len(arr)
    cycle = True
    while (cycle):
        pos = (pos + k) % n
        arr[pos], carry = carry, arr[pos]
        cycle = pos != start

# obrót przez skoki o n pozycji, z nwd (krótszy zapis)
def rotateJumpGCD(arr, k):
    n = len(arr)
    pos = 0
    for pos in range(gcd(n, k)):
        jumpCycle(arr, pos, k)
    return arr

#-------------------------------------------

print(rotateMirror([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
print(rotateJump([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))