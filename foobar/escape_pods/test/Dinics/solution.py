from collections import deque

def clone_path(x):
    return = [row[:] for row in x]

def augment_paths(c, f):
    paths = clone_path(c)
    for u in range(len(c)):
        for v in range(len(c)):
            paths[u][v] = c[u][v] - f[u][v]
            paths[v][u] = f[u][v]
    return paths

def n_by_m(n, m):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat[i].append(0)
    return mat

def blocking_path(entrances, exits, rooms):
    crumbs = [0] * len(rooms)
    flow = n_by_m(len(rooms), len(rooms))
    for e in entrances:
        crumbs[e] = 1
    for e in exits:
        crumbs[e] = -1
    
    def send(n, r):
        if crumbs[r] == -1:
            return 0

        N = n
        crumbs[r] += 1
        for i, b in enumerate(rooms[r]):
            if n == 0:
                break
            if b == 0 or crumbs[i] > 0:
                continue
            if b > n:
                b = n
            sent = send(b, i)
            flow[r][i] += sent
            rooms[r][i] = rooms[r][i] - b + sent
            n -= b - sent

        if N > n:
            crumbs[r] -= 1
        return n

    MAX = 2000000
    not_sent = 0
    for ent in entrances:
    	not_sent += send(MAX, ent)
    return flow



def layered_graph(paths):
    layers = [-1] * len(paths)
    layers[0] = 0
    queue = deque([0])
    while len(queue) > 0:
        q = queue.popleft()
        for i, c in enumerate(paths[q]):
            if c != 0 and layers[i] == -1:
                layers[i] = layers[q] + 1
                queue.append(i)
    return layers    

# assume super entrance node and super exit node
def super_nodes(ens, exs, paths):
    MAX = 2000000 # practical infinity for the problem
    n = len(paths) + 2
    edges = [[0] * n]
    exits = [[0] * n]
    for i in range(len(paths)):
        if i in ens:
            edges[0][i + 1] = MAX
        edges.append([0] + list(paths[i]) + [0])
        if i in exs:
            edges[i + 1][-1] = MAX
    return edges + exits

# main answer
def answer(ens, exs, paths):
    paths = super_nodes(ens, exs, paths)
    c = clone_path(paths)
    while True
        gl = layered_graph(paths)
        if gl[-1] == -1:
            return "DONE"
        
        

# tests
def test(ens, exs, path, exp):
    res = answer(ens, exs, path)
    if res != exp:
        print("Failed")
        print(ens, exs, path)
        print(" got=", res)
        print(" exp=", exp)

# tough test
test([0], [5], [
    [0, 10, 10, 0, 0, 0],
    [0, 0, 2, 4, 8, 0],
    [0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 10],
    [0, 0, 0, 6, 0, 10],
    [0, 0, 0, 0, 0, 0]
], 19)
