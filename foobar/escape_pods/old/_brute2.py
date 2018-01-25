def answer(entrances, exits, rooms):
    bread_crumbs = [0] * len(rooms)
    for e in entrances:
        bread_crumbs[e] = 1
    exs = {}
    max_out = [0]
    for e in exits:
        exs[e] = True
        for r in rooms:
            max_out[0] += r[e]

    max_out.append(max_out[0])
    
    def send(n, r):
        if r in exs:
            max_out[0] -= n
            #print("EXIT", n)
            return 0

        bread_crumbs[r] += 1
        #print("send", n, r)
        for i, b in enumerate(rooms[r]):
            if max_out[0] == 0:
                raise BaseException(max_out[1])
            if n == 0:
                break
            if b == 0 or i == r or bread_crumbs[i] > 0:
                continue
            #print(b, "from", r, "to", i, "with", n, "left")
            if b > n:
                b = n
            sent = send(b, i)
            rooms[r][i] = rooms[r][i] - b + sent
            n -= b - sent

        bread_crumbs[r] -= 1
        #print(n, "left")
        return n

    try:
        MAX = 2000000
        not_sent = 0
        for ent in entrances:
            not_sent += send(MAX, ent)
    
        return MAX * len(entrances) - not_sent
    except BaseException:
        return max_out[1]

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
        (size - 1)  * n + 1 
    )

test_complexity(17, 5)
test_complexity(22, 5)

raise "TOO slow"
test_answer(
    list(range(10)),
    [28],
    [
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29,
        [3] * 29
    ],
    1000
)
