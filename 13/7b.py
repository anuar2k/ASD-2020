#zad 7.2
def intersection(A,B):
    counter =0
    for element in (A):
        if element.state == BUSY:
            if find(B, element.key):
                counter+=1
    return counter