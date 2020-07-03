# TODO: Naprawic bo zle XD

def abs(x):
    return x if x >= 0 else -x

def opt_sum(tab):
    result = 0

    while len(tab) > 1:
        minpair_idx = 0
        # szukamy minimalnej pary, O(n)
        for i in range(1, len(tab) - 1):
            if abs(tab[minpair_idx] + tab[minpair_idx + 1]) > abs(tab[i] + tab[i + 1]):
                minpair_idx = i

        new_sum = tab[minpair_idx] + tab[minpair_idx + 1]

        # zastępujemy parę nową liczbą w zadanym miejscu
        # usunięcie elementu z środka listy jest O(n), co nie psuje nam złożności, bo znalezienie
        # minimalnej pary też jest O(n)
        tab[minpair_idx] = new_sum
        tab.pop(minpair_idx + 1)

        if abs(new_sum) > result:
            result = abs(new_sum)

    return result

