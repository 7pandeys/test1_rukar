from string import punctuation

str = "He is, a well-known person. As a person I know him well"


def nlp(str):
    for i in str:
        if i in punctuation:
            str = str.replace(i, " ")
    str = str.lower()
    # print(str)
    str = " ".join(str.split())
    l = str.split(" ")
    s1 = []
    s2 = []

    d = {}
    for i in l:
        if i in d.keys():
            d[i] = d[i]+1
            s1.append(i)
        else:
            d[i] = 1
    # print(d)
    # print(s1)
    l.clear()
    l = list(d.keys())
    for i in l:
        if i not in s1:
            s2.append(i)
    s2.sort()
    l.clear()
    # l=s1
    # print(s2)
    s = " ".join(s1 + s2)
    print(s)


nlp(str)
