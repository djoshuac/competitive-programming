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

def make_nodes(edges, values):
    class Node:
        def __init__(self, id, value):
            self.id = id
            self.value = value
            self.children = []
            self.edge_sizes = {}

    edges = list(map(lambda e: list(sorted([e[0] - 1, e[1] - 1])), edges))

    nodes = [Node(i, v) for i, v in enumerate(values)]
    for e in edges:
        nodes[e[0]].children.append(nodes[e[1]])

    def bfs(u, v, count_from):
        if u != None:
            v.edge_sizes[u.id] = count_from
        total = 0
        for c in v.children:
            count_to = bfs(v, c, count_from + 1)
            v.edge_sizes[c.id] = count_to
            total += count_to
        return total + 1
    print(bfs(None, nodes[0], 0))

    for n in nodes:
        print("-------", n.id, "--------")
        for k in n.edge_sizes.keys():
            print(n.id, "to", k, "is", n.edge_sizes[k], "long")





def sum_of_fibonacci_edges(edges, values):
    modulo = 10**9 + 7
    fib = create_fibber(modulo)

    make_nodes(edges, values)

if __name__ == "__main__":
    edges = [list(sorted(map(int, input().split()))) for _ in range(int(input()) - 1)]
    values = list(map(int, input().split()))
    print(sum_of_fibonacci_edges(edges, values))
