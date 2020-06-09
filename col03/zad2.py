# Zasada działania jest taka:
# dla każdego klucza jaki mamy w tablicy sprawdzamy czy da się go znaleźć - jeśli się nie da znaleźć danego
# elementu, to zwracamy pozycję, w której jest dziura. Od pozycji dziura + 1 robimy zepchnięcia następnych
# elementów do tyłu o 1 pozycje, jesli ma to sens oczywiscie (bo w tym ciagu moze sie trafic element na swoim miejscu)
# Ciąg takich zepchnięć przerywamy, gdy:
# a) znaleźliśmy element, który nie wymaga zepchnięcia
# b) znaleźliśmy naturalną dziurę
# Złożoność algorytmu wynosi w przybliżeniu O(n) (możemy przesunac wiekszosc tablicy o 1 pozycje do tylu, a find jest raczej O(1))

# Możnaby też upchnąć w dziurę po prostu taken = True (jako "keep looking") - ale to byłoby za proste? + None nie jest prawidłowym kluczem

class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        
    def __str__(self):
        if not self.taken:
            print('pusty')
        else:
            print('klucz: ', self.key)

def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N

N=11
hash_tab = [Node() for i in range(N)]

def find_break_pos(hash_tab, key):
    idx = h(key)
    for _ in range(N):
        if not hash_tab[idx].taken: return idx
        if hash_tab[idx].key == key: return None
        idx = (idx + 1) % N

    #do tego returna nigdy nie wyjdzie, bo wolamy find_break_pos tylko dla wartosci, ktore istnieja/maja istniec
    return None
    
def push_down(hash_tab, i):
    src = i
    node = hash_tab[i]

    if not node.taken:
        return False

    idx = h(node.key)

    # jesli element nie jest na swojej pozycji to naturalnie musimy go cofnac
    if i != idx:
        i = (i - 1) % N
        hash_tab[i].taken = node.taken
        hash_tab[i].key = node.key
        hash_tab[src].taken = False
        hash_tab[src].key = None
        return True
    
    return False

def recover(hash_tab):
    breakpos = None

    # szukamy dziury w całym - zakładając, że find_break_pos jest O(1) to całość jest O(n)
    for node in hash_tab:
        if node.taken:
            pos = find_break_pos(hash_tab, node.key)
            if pos is not None:
                breakpos = pos
                break

    if breakpos:
        # w przybliżeniu N powtórzeń zepchnięć, co daje razem O(N)
        for i in range(1, N):
            # spychamy oczywiscie o nie wiecej niz 1 pozycje, bo dziura jest szerokosci 1
            # przerywamy spychac, jak dzieja sie przypadki lit. a lub b z opisu wyzej
            # zepchniecia sa O(1)
            if not push_down(hash_tab, (i + breakpos) % N):
                break
