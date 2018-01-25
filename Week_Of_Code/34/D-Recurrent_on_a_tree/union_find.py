#!/bin/python3

def create_fibber(modulo):
    memo = {
        0: 0,
        1: 1,
        2: 1,
        3: 2
    }
    def fib(n):
        def recurse(n):
            if not n in memo:
                if n % 2 == 0:
                    k = n // 2
                    memo[k] = recurse(k)
                    memo[k - 1] = recurse(k - 1)
                    memo[n] = ((2 * memo[k - 1] + memo[k]) * memo[k]) % modulo
                else:
                    k = (n + 1) // 2
                    memo[k] = recurse(k)
                    memo[k - 1] = recurse(k - 1)
                    memo[n] = (memo[k]**2 + memo[k -1]**2) % modulo
            return memo[n]
        return recurse(n + 1)
    return fib

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.d = value
        self.children = []
        self.ancestor = self
        self.done = False
        self.parent = self
        self.rank = 0
        self.depth = 0

def find(x):
    while x != x.parent:
        x = x.parent
    return x

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root.rank < y_root.rank:
        y_root.parent = x_root
    elif x_root.rank > y_root.rank:
        x_root.parent = y_root
    else:
        y_root.parent = x_root
        x_root.rank += 1

def sum_of_fibonacci_edges(edges, values):
    nodes = [Node(i, v) for i, v in enumerate(values)]

    for e in edges:
        nodes[e[0] - 1].children.append(nodes[e[1] - 1])

    modulo = 10**9 + 7
    fib = create_fibber(modulo)

    lca = {}
    def targan_olca(u):
        for v in u.children:
            targan_olca(v)
            union(u, v)
            find(u).ancestor = u
        u.done = True
        for v in nodes:
            if v.done:
                p = tuple(sorted([u.id, v.id]))
                lca[p] = find(v).ancestor
    targan_olca(nodes[0])

    def bfs(u, depth):
        u.depth = depth
        for v in u.children:
            bfs(v, u.depth + u.value)
    bfs(nodes[0], 0)

    s = 0
    for i, u in enumerate(nodes):
        for j in range(i, len(nodes)):
            if i == j:
                s += fib(u.value)
            else:
                v = nodes[j]
                p = (u.id, v.id)
                dist = u.depth + v.depth - 2*lca[p].depth - lca[p].value + u.value + v.value
                s += fib(dist) * 2
    return s

# if __name__ == "__main__":
#     edges = [tuple(sorted(list(map(int, input().split())))) for _ in range(int(input()) - 1)]
#     values = list(map(int, input().split()))
    # print(sum_of_fibonacci_edges(edges, values))

#
# edges = [
#     (0, 1),
#     (0, 6),
#     (1, 2),
#     (1, 3),
#     (3, 4),
#     (4, 5),
#     (6, 7),
#     (6, 8),
#     (6, 9)
# ]
#
# values = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]

edges = [
    (1, 2),
    (1, 3)
]
values = [2, 1, 1]

print(sum_of_fibonacci_edges(edges, values))
