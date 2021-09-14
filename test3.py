from math import sqrt
l = [(1, 1), (4, 3), (5, 8), (9, 4), (2, 4), (5, 5)]
# √[(x2 – x1)2 + (y2 – y1)2].


def euc(l):

    x1, y1, tmp = 0, 0, 0
    for i in l:
        # print(i)
        x = i[0]
        y = i[1]
        f = sqrt((x**2 + y**2))
        if tmp < f:
            tmp = f
            x1 = x
            y1 = y
    print((x1, y1))

    # else:


euc(l)
