import sys
from collections import defaultdict
from operator import itemgetter
from itertools import groupby
import collections

listpair = []

first = input()
x, y = first.split()

x = int(x)

for pair in range(int(y)):
    rest = input()
    a, b = rest.split()
    listpair.append([int(a), int(b)])


def build_graph():
    edges = listpair
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge[0], edge[1]

        graph[a].append(b)
        graph[b].append(a)
    return graph


if __name__ == "__main__":
    graph = build_graph()

di = dict(graph)


def check(di, x):
    a = list(di.keys())
    z = len(a)
    dct = di
    for key in dct:
        if len(dct[key]) < 5 or len(dct[key]) > (z - 5):
            del dct[key]
            for v in dct.values():
                tok = v
                Deque = collections.deque(tok)
                if key in Deque:
                    Deque.remove(key)
            return check(dct, z)

    l = list(dct.keys())
    n = len(l)
    print(n)
    print(*l)


check(di, x)