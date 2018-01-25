def answer(entrances, exits, rooms):
    crumbs = [0] * len(rooms)
    for e in entrances:
        crumbs[e] = 1
    for e in exits:
        crumbs[e] = -1
    
    def send(n, r):
        if crumbs[r] == -1:
            #print("EXIT", n)
            return 0

        N = n
        crumbs[r] += 1
        #print("send", n, r)
        for i, b in enumerate(rooms[r]):
            if n == 0:
                break
            if b == 0 or crumbs[i] > 0:
                continue
            #print(b, "from", r, "to", i, "with", n, "left")
            if b > n:
                b = n
            sent = send(b, i)
            rooms[r][i] = rooms[r][i] - b + sent
            n -= b - sent

        if N > n:
            crumbs[r] -= 1
        #print(n, "left")
        return n

    MAX = 2000000
    not_sent = 0
    for ent in entrances:
    	not_sent += send(MAX, ent)
    return MAX * len(entrances) - not_sent

def test_answer(ent, exi, rooms, exp):
    got = answer(ent, exi, rooms)

    if got != exp:
        print("Failed for ", ent, exi, rooms, "  exp=", exp, "  got=", got)



test_answer([0, 1], [4, 5], [
    [0, 0, 4, 6, 0, 0],
    [0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 4, 4],
    [0, 0, 0, 0, 6, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
], 16)

test_answer([0], [3], [
    [0, 7, 0, 0],
    [0, 0, 6, 0],
    [0, 0, 0, 8],
    [9, 0, 0, 0]
], 6)


test_answer([0, 1], [6], [
    [0, 0, 2, 2, 2, 10, 0],
    [0, 0, 2, 2, 2, 5, 0],
    [0, 0, 0, 0, 1, 0, 2],
    [0, 0, 0, 0, 1, 0, 2],
    [0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 12],
    [0, 0, 0, 0, 0, 0, 0]
], 20)

print("")
print("")
print("Testing Cycles")

test_answer([0], [5], [
    [0, 10, 0, 0, 0, 0],
    [0, 0, 10, 5, 10, 0],
    [10, 10, 10, 0, 0, 0],
    [0, 0, 10, 0, 0, 0],
    [0, 0, 0, 0, 0, 10],
    [10, 10, 10, 10, 10, 0]
], 10)


def test_complexity(size, n):
    paths = []
    for x in range(size):
        paths.append([n] * size)
    
    test_answer(
        list(range(size // 3)),
        [size - 1],
        paths,
        (size - 1)  * n
    )

test_complexity(17, 5)
test_complexity(22, 5)
test_complexity(30, 5)
test_complexity(100, 20)