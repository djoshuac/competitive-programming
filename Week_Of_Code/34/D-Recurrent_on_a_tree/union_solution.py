#!/bin/python3

def create_fibber(modulo):
    memo = {
        0: 1,
        1: 1,
        2: 2
    }
    def fib(n):
        if not n in memo:
            if n % 2 == 0:
                k = n // 2
                memo[k] = recurse(k)
                memo[k - 1] = fib(k - 1)
                memo[n] = ((2 * memo[k - 1] + memo[k]) * memo[k]) % modulo
            else:
                k = (n + 1) // 2
                memo[k] = fib(k)
                memo[k - 1] = fib(k - 1)
                memo[n] = (memo[k]**2 + memo[k -1]**2) % modulo
        return memo[n]
    return fib

def create_lca_nodes(edges, values):
    class Node:
        def __init__(self, id, value):
            self.id = id
            self.value = value
            self.d = value
            self.children = []
            self.parent = self
            self.rank = 0
            self.ancestor = self
            self.done = False

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x.rank > root_y.rank:
            root_y.parent = root_x
        elif root_x.rank < root_y.rank:
            root_x.parent = root_y
        else:
            y_root.parent = x_root
            x_root.rank += 1

    def find(x):
        while x.parent != x:
            x = x.parent
        return x

    lca = {}
    def targan(u):
        for v in u.children:
            targan(v)
            union(u, v)
            find(u).ancestor = u
        u.done = True
        for v in u.children:
            if v.done == True:
                a, b = u.id, v.id
                lca[(a, b)] = lca[(b, a)] = find(v).ancestor

    nodes = [Node(i, v) for i, v in enumerate(values)]

    for e in edges:
        x, y = e[0] - 1, e[1] - 1
        x, y = x, y if x < y else y, x
        nodes[x].children.append(nodes[y])
        nodes[y].ancestor = nodes[x]

    targan(nodes[0])

    # figure out how far away all the nodes are from the root: nodes[0]
    # dist = d(a) + d(b) - 2*d(lca(a, b))
    # sum fib(dist(u, v)) for all pairs u v -- maybe skip uu and vv pairs


def sum_of_fibonacci_edges(edges, values):
    modulo = 10**9 + 7
    fib = create_fibber(modulo)

    s = 0
    for v in values:
        s += fib(v)
    return s

    dist = []
    for v in values:
        dist.push()

if __name__ == "__main__":
    edges = [list(map(int, input().split())) for _ in range(int(input()))]
    values = list(map(int, input().split()))
    print(sum_of_fibonacci_edges(edges, values))
