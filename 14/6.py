class Zestaw:
    def __init__(self):
        self.len = 1
        self.end = self

def trains(links):
    zajezdnia = {}
    for wagon in set([wagon for link in links for wagon in link]):
        zajezdnia[wagon] = Zestaw()

    result = 0
    for link in links:
        zestawA = zajezdnia[link[0]]
        zestawB = zajezdnia[link[1]]

        newLen = zestawA.len + zestawB.len

        if newLen > result:
            result = newLen

        tmp = zestawA.end
        zestawA.end.end = zestawB.end
        zestawB.end.end = tmp

        zestawA.len = newLen
        zestawB.len = newLen
        zestawA.end.len = newLen
        zestawB.end.len = newLen

    return result

links = [(1, 2), (2, 3), (5, 6), (6, 7), (4, 5)]
print(trains(links))




