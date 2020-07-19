# Algorytm sortuje liczby na podstawie dwóch kryteriów z treści zadania
# wykorzystujemy tutaj podejście podobne do radix sorta (sortowanie wg coraz ważniejszych kryteriów),
# więc stabilnie sortujemy za pomocą counting sorta (ktory sortuje wartosci od 0 do 10 jako liczba liczb jedno/wielokrotnych)
# mniej ważnym kryterium jest liczba cyfr wielokrotnych, wazniejszym - liczba cyfr jednokrotnych

# zlozonosc algorytmu wynosi O(nd + n + n) = O(nd) gdzie d to liczba cyfr
# co wynika z kroków zliczania liczb jedno/wielokrotnych i dwukrotnego sortowania O(n)

# wybor counting sorta wynika z tego, ze jest on stabilny (nadaje sie do radix sorta) i sortuje
# on bardzo ograniczony zakres wartosci (0 - 10 wystąpień)

# key to funkcja, która wyłuskuje wartość, na podstawie której sortujemy
# descending - kierunek malejący


def counting_sort(T, key, descending):
    hist = [0] * 11 #wartosci od 0 do 10

    for elem in T:
        hist[key(elem)] += 1

    if descending:
        for i in range(len(hist) - 2, -1, -1):
            hist[i] += hist[i + 1]
    else:
        for i in range(1, len(hist)):
            hist[i] += hist[i - 1]
        

    result = [None] * len(T)
    for i in range(len(T) - 1, -1, -1):
        hist[key(T[i])] -= 1
        result[hist[key(T[i])]] = T[i]

    return result

def pretty_sort(T):
    # przygotowuje krotki zawierajace informacje o kazdej liczbie, by ich nie generowac wielokrotnie

    # O(nd)
    for i in range(len(T)):
        number = T[i]
        digits = [0] * 10

        # O(d), to zalezy od tego, ile cyfr ma liczba
        while T[i] > 0:
            digits[T[i] % 10] += 1
            T[i] //= 10

        single = 0
        multiple = 0

        for digit in digits:
            if digit == 1:
                single += 1
            elif digit > 1:
                multiple += 1

        T[i] = (number, single, multiple)

    # sortujemy najpierw rosnąco wg ilosci cyfr wielokrotnych, bo im wiecej tym gorzej, klucz: krotka[2]
    # O(n)
    T = counting_sort(T, lambda x: x[2], False)
    # sortujemy potem malejąco wg ilosci cyfr pojedycznych, bo im wiecej tym lepiej, klucz: krotka[1]
    # O(n)
    T = counting_sort(T, lambda x: x[1], True)
    
    # przywracamy wynik z naszych krotek z dodatkowymi danymi
    return [x[0] for x in T]

print(pretty_sort([123, 455, 1266, 114577, 2344, 67333, 1234567890]))
