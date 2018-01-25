#!/bin/python3
from collections import deque

def circularWalk(n, s, t, r_0, g, seed, p):
    r = [0] * n
    r[0] = r_0
    for i in range(1, n):
        r[i] = (r[i - 1] * g + seed) % p

    if s == t:
        return 0

    bfs = deque()
    visited = {}
    visited[s] = True
    bfs.append((s, 1))
    best = n + 1
    while bfs:
        i, depth = bfs.popleft()
        low = (i + n - r[i]) % n
        high = (i + r[i]) % n
        if low == high and r[i] > 0:
            if depth < best:
                best = depth
                continue
        j = low
        print(low, t, high, "from", s)
        while True:
            if j == t and depth < best:
                best = depth
            if not j in visited:
                visited[j] = True
                bfs.append((j, depth + 1))
            j = (j + 1) % n
            if (j == (high + 1) % n):
                break;
    if best == n + 1:
        return -1
    else:
        return best


n, s, t = input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
