l = ['$40k', '$400', '$805', '$1.5b', '$2.2m', '$7.5m', '$6.5b', '$1000']


def curr(l):

    l1 = list(map(lambda a: str(a), l))
    l.clear()
    l = l1
    b = []
    m = []
    k = []
    t = []
    for i in l:
        if 'b' in i:
            b.append(i)
        elif 'm' in i:
            m.append(i)
        elif 'k' in i:
            k.append(i)
        else:
            t.append(i)
    print(b + m + k + t)


curr(l)
