# Aleksander Wójtowicz, 400184
class Node:
    def __init__(self, pos, left, right):
        self.left = left
        self.right = right
        self.pos = pos
        self.height = 0

def arr_to_bst(arr, left, right):
    if left > right:
        return None

    middle = (left + right) // 2
    return Node(arr[middle], arr_to_bst(arr, left, middle - 1), arr_to_bst(arr, middle + 1, right))

def max_height(bst, a, b):
    if bst is None:
        return 0

    if bst.pos < a:
        return max_height(bst.right, a, b)
    elif bst.pos > b:
        return max_height(bst.left, a, b)
    else:
        return max(bst.height, max_height(bst.left, a, b), max_height(bst.right, a, b))

def update_height(bst, a, b, height):
    if bst is not None:
        if bst.pos < a:
            update_height(bst.right, a, b, height)
        elif bst.pos > b:
            update_height(bst.left, a, b, height)
        else:
            bst.height = height
            update_height(bst.left, a, b, height)
            update_height(bst.right, a, b, height)

# Główna idea: trzymamy wysokość słupka w BST
# Mam wątpliwości, czy ten algorytm może się ukwadratowić. Z jednej strony może się zdarzyć,
# że kładziemy klocek nad wszystkimi innymi i wtedy max_height oraz update_height są O(n),
# co przy n klockach dawałoby O(n^2), no ale z drugiej strony - największy klocek jest tylko jeden,
# więc może przy użyciu analizy zamortyzowanej to by się wybroniło do O(nlogn)?
def bricks(K):
    # generujemy z listy klocków listę możliwych "słupków", O(nlogn) - przez sortowanie
    positions = [pos for tup in K for pos in tup]
    positions.sort()

    # z posortowanej listy krawędzi klocków robimy listę unikalnych krawędzi
    uniq_positions = [positions[0]]
    for pos in positions:
        if uniq_positions[len(uniq_positions) - 1] != pos:
            uniq_positions.append(pos)

    # generujemy BST z krawędzi - O(n)
    bst = arr_to_bst(uniq_positions, 0, len(uniq_positions) - 1)

    result = 0
    # n powtórzeń razy... no właśnie? Ciało funkcji jest O(n), ale czy finalnie wynik będzie O(n^2)?
    # w końcu pesymistyczny przypadek zdarza się tylko raz
    for brick in K:
        # kolejny klocek przykryje wszystkie pod nim, i będzie na wysokości o 1 większej od najwyższego pod
        height = 1 + max_height(bst, brick[0], brick[1])
        if height > result:
            result = height
        update_height(bst, brick[0], brick[1], height)

    return result

print(bricks([(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]))