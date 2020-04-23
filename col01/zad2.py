# możemy tutaj wykorzystać quickSelecta, ktory ma zlozonosc O(n) (zakladawszy, ze nie wpadamy w przypadek pesymistyczny)
# wykorzystujemy tutaj wlasnosc quickselecta, ze wszystkie elementy na lewo od k-tej najmniejszej
# beda mniejsze od niej, a wszystkie elementy na prawo od k-tej najmniejszej beda wieksze od niej - to nam pozwala uzyskac wynik
# bez sortowania calej tablicy. To bardzo wazne, by drugi quickSelect wywolac w zawezonym przedziale tak, by nie zepsuc uzyskanej
# wyzej opisanej wlasnosci. Uruchomienie drugiego quickSelecta na przedziale od 0 do n-1 moze przerzucic nam 
# elementy wieksze od k-tego ponizej pozycji k (może to zrobić partition)

# Zlozonosc wynosi O(n + n + n) (2*quickselect + przepisanie wartosci do tablicy wynikowej)
import random

def partition(T, low, high):
    # randomizacja, to po to, by zmiejszyc szanse na przypadek pesymistyczny
    pivot = random.randint(low, high)
    T[high], T[pivot] = T[pivot], T[high]

    split = low
    for i in range(low, high):
        if T[i] < T[high]:
            T[i], T[split] = T[split], T[i]
            split += 1

    T[split], T[high] = T[high], T[split]
    return split

def quickSelect(T, low, high, n):
    # funkcja nie zwraca wybranej n-tej wartosci, bo nie uzywamy jej do wyliczenia wyniku
    while low < high:
        pivot = partition(T, low, high)
        if pivot == n:
            return
        if pivot < n:
            low = pivot + 1
        else:
            high = pivot - 1

def section(T, p, q):
    n = len(T)
    # skoro nasi zolnierze se ustawieni malejaco wg wzrostu, to zamiast wypierac p-tą wartosc wybieramy (n - 1 - p)tą
    # a potem (n - 1 - q)tą
    quickSelect(T, 0, n - 1, n - 1 - p)
    # w drugim wywolaniu musimy zawezic obszar dzialania quickselecta, by nie zepsuc opisanej w wytlumaczeniu wlasciwosci
    quickSelect(T, 0, n - 1 - p, n - 1 - q)
    # dodajemy odwrotnie elementy by uzyskac odpowiednia kolejnosc
    result = [None] * (q - p + 1)
    idx = 0
    for i in range(n - 1 - p, n - 1 - q - 1, -1):
        result[idx] = T[i]
        idx += 1

    return result

tab = [6, 7, 8, 1, 2, 3, 5, 4]
print(section(tab, 2, 5))
