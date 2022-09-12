grah = {'0': set(['1', '2']),
        "1": set(["3", "0"]),
        "2": set(["0"]),
        "3": set(["1", "4"]),
        "4": set(["3"])}

visit = []
qout = []
s = -1


def breadth_first_search(grah, start, visit, qout, s):
    if start not in visit:
        for v in grah[start]:
            if v not in qout:
                qout.append(v)
    visit.append(start)
    if len(grah) > len(qout):
        s += 1

        breadth_first_search(grah, qout[s], visit, qout, s)
    return qout


print(breadth_first_search(grah, '1', visit, qout, s))
