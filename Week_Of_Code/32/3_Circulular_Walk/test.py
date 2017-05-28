from collections import deque

def circularWalkBrute(n, s, t, r_0, g, seed, p):
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
        if n / 2 <= r[i]:
            if depth < best:
                best = depth
                continue
        j = low
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
    # r = [0] * n
    # r[0] = r_0
    # for i in range(1, n):
    #     r[i] = (r[i - 1] * g + seed) % p
    #
    # if s == t:
    #     return 0
    #
    # bfs = deque()
    # visited = {}
    # visited[s] = True
    # bfs.append((s, 1))
    # best = n + 1
    # while bfs:
    #     i, depth = bfs.popleft()
    #     low = (i + n - r[i]) % n
    #     high = (i + r[i]) % n
    #     j = low
    #     while True:
    #         if j == t and depth < best:
    #             best = depth
    #         if not j in visited:
    #             visited[j] = True
    #             bfs.append((j, depth + 1))
    #         j = (j + 1) % n
    #         if (j == (high + 1) % n):
    #             break;
    # if best == n + 1:
    #     return -1
    # else:
    #     return best

def circularWalk(n, s, t, r_0, g, seed, p):
    def standardize(i):
        return (i + n - t) % n
    zero = standardize(0)
    r = [0] * n
    r[zero] = r_0
    i = (zero + 1) % n
    while i != zero:
        r[i] = (r[(i + n - 1) % n] * g + seed) % p
        i = (i + 1) % n
    s = standardize(s)

    if s == 0:
        return 0

    ll = s
    hh = s
    l = s - r[s]
    h = s + r[s]

    depth = 1
    while l < ll or h > hh:
        lll = ll
        hhh = hh
        ll = l
        hh = h
        if l <= 0 or h >= n:
            return depth

        depth += 1
        j = ll
        while j != lll:
            low = j - r[j]
            if low < l:
                l = low
            high = j + r[j]
            if high > h:
                h = high
            j = (j + 1) % n
        j = hh
        while j != hhh:
            low = j - r[j]
            if low < l:
                l = low
            high = j + r[j]
            if high > h:
                h = high
            j = (j + n - 1) % n

    return -1


if __name__ == "__main__":
    N = 100
    S = 31
    for n in range(S, N):
        print("n", n)
        for s in range(n):
            print("s", n, s)
            for t in range(n):
                print("t", t)
                for p in range(1, n):
                    print("p", p, t)
                    for r in range(p):
                        for g in range(p):
                            for seed in range(p):
                                cwb = circularWalkBrute(n, s, t, r, g, seed, p)
                                cw = circularWalk(n, s, t, r, g, seed, p)
                                if cwb != cw:
                                    print("FAIL", cwb, cw)
                                    print(n, s, t, r, g, seed, p)
                                    raise "NO"
                    # r = 1
                    # g = 0
                    # seed = 0
                    # cwb = circularWalkBrute(n, s, t, r, g, seed, p)
                    # cw = circularWalk(n, s, t, r, g, seed, p)
                    # if cwb != cw:
                    #     print("FAIL", cwb, cw)
                    #     print(n, s, t, r, g, seed, p)
                    #     raise "NO"
                    # g = 1
                    # seed = 10
                    # cwb = circularWalkBrute(n, s, t, r, g, seed, p)
                    # cw = circularWalk(n, s, t, r, g, seed, p)
                    # if cwb != cw:
                    #     print("FAIL", cwb, cw)
                    #     print(n, s, t, r, g, seed, p)
                    #     raise "NO"
                    # g = 31
                    # seed = 14
                    # cwb = circularWalkBrute(n, s, t, r, g, seed, p)
                    # cw = circularWalk(n, s, t, r, g, seed, p)
                    # if cwb != cw:
                    #     print("FAIL", cwb, cw)
                    #     print(n, s, t, r, g, seed, p)
                    #     raise "NO"
