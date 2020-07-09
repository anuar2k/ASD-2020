# Skoro liczby to a^x, gdzie x jest o rozkładzie jednostajnym, to należy wykorzystać bucket sorta
# gdzie krawędzie bucketów, to będzie kolejne wartości a^k, gdzie k = n/liczba_elementów
# aby uzyskać numer bucketa musimy odwrócić operację potęgowania, więc wykorzystujemy logarytm.
# Kazdy z bucketów jest na tyle maly (proporcja liczby bucketow do liczby danych jest stala),
# ze mozemy go posortowac jakas prosta metoda sortowania zakladajac w przyblizeniu zlozonosc stala.
# W ten sposob zrobimy n bucketów * operacje w czasie ok. O(1), co daje nam zlozonosc O(n)

# Zakładam, że lista pythonowa jest listą z 2 końcami, co pozwala na append w czasie O(1)
# wpp moznaby wykorzystac wlasna implementacje listy odsylaczowej

import math

def insertion_sort(tab):
    n = len(tab)
    
    for i in range(1, n):
        to_insert = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > to_insert:
            tab[j + 1] = tab[j]
            j -= 1

        tab[j + 1] = to_insert

def bucketSort(tab, a, low = 0, high = 1):
    n = len(tab)

    if n <= 1:
        return tab

    # Tworzymy n kubełków, O(n)
    buckets = [[] for _ in range(n)]

    # dodajemy kazdy element do kubelka, O(n)
    for elem in tab:
        # dalsze operacje w tej pętli są w czasie stałym
        buckIdx = math.floor((math.log(elem, a) - low) / (high - low) * n)
        if buckIdx == n:
            buckIdx = n - 1
        buckets[buckIdx].append(elem)

    # sortujemy kazdy kubelek, O(1) * n = O(n)
    for i in range(n):
        insertion_sort(buckets[i])

    result = []

    # złączamy kubełki, O(n) (wyobrazamy sobie, ze zlaczamy listy, ktore maja poczatek i koniec)
    for bucket in buckets:
        result += bucket

    return result

def fast_sort(tab, a):
    return bucketSort(tab, a)
