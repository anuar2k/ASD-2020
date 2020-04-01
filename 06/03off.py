def csortBy(A, idx):
    # przygotowujemy histogram - szukamy zakresu wartosci
    minVal = A[0][idx]
    maxVal = A[0][idx]

    n = len(A)

    for i in range(1, n):
        if A[i][idx] < minVal:
            minVal = A[i][idx]
        if A[i][idx] > maxVal:
            maxVal = A[i][idx]

    # utworzenie histogramu
    histSize = maxVal - minVal + 1
    hist = [0] * histSize

    # wypelnienie go danymi
    for elem in A:
        hist[elem[idx] - minVal] += 1

    # sumy prefiksowe
    for i in range(1, histSize):
        hist[i] += hist[i - 1]
    
    # rozmieszczenie elementow do tablicy wynikowej
    Asorted = [None] * n
    for i in range(len(A) - 1, -1, -1):
        hist[A[i][idx] - minVal] -= 1
        Asorted[hist[A[i][idx] - minVal]] = A[i]
    return Asorted

def knapsack(A, k):
    # w tym przypadku wybierajac plyn, ktory wrzucimy do plecaka liczy sie wartosc za litr, stad musimy przeksztalcic dane:
    for i in range(len(A)):
        A[i] = (A[i][0] // A[i][1], A[i][1])

    # majac juz cene za litr kazdego plynu, pobieramy dopoki mamy miejsce te plyny o najwiekszej wartosci

    # z przykladowych danych wynika, ze sa to dane calkowite - jesli nie, sortowanie przez zliczanie mozna zastapic jakims innym O(nlogn)
    A = csortBy(A, 0)

    # poniewaz nasze dane sa posortowane rosnaco wg wartosci za litr, idziemy od konca
    pos = len(A) - 1
    result = 0

    while pos >= 0 and k > 0:
        # pobieramy tyle, ile sie da
        to_drain = min(A[pos][1], k)
        # wartosc zwieksza sie o ilosc pobranego plynu razy cena za litr
        result += A[pos][0] * to_drain
        # odejmujemy pobrana objetosc
        k -= to_drain
        # wybieramy kolejny zbiornik o nizszej wartosci za litr
        pos -= 1
    return result

print(knapsack([(1, 1), (10, 2), (6, 3)], 3))