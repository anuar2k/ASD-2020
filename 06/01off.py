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


def tasks(A):
    # krok 1: sortowanie przez zliczanie, kryterium: koniec zajec
    A = csortBy(A, 1)

    # krok 2:
    # poniewaz elementy sa posortowane wg czasu zakonczenia zajec, bierzemy element 
    # pierwszy dostepny, ten element wziety na pewno konczy sie najwczesniej. Od tego momentu pomijamy 
    # kolejne czasy, ktore maja poczatek wczesniejszy, niz koniec wzietego (one koliduja), a mozemy to robic liniowo
    # bo mamy czasy posortowane wg konca
    result = 0
    curr = 0
    while curr < len(A):
        # bierzemy najwczesniej konczace sie zajecia...
        selected = A[curr]
        result += 1
        curr += 1
        # i pomijamy wszystkie kolizyjne
        while curr < len(A) and A[curr][0] < selected[1]:
            curr += 1

    return result

print(tasks([(0, 10), (10, 20), (5, 15)]))