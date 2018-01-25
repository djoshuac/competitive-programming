def get_string_length(strings, places):
    m = 0
    for s, p in zip(strings, places):
        m = max(m, len(s) + p[-1])
    return m

def reconstruct(strings, places):
    solution = bytearray()
    solution.extend(map(ord, ['a'] * get_string_length(strings, places)))

    for s, pla in zip(strings, places):
        bs = bytearray()
        bs.extend(map(ord, s))
        for p in pla:
            solution[p:p+len(s)] = bs

    return solution.decode('utf-8')

if __name__ == "__main__":
    strings = []
    places = []
    for _ in range(int(input())):
        line = input().split()
        strings.append(line[0])
        p = []
        for ki in range(int(line[1])):
            p.append(int(line[ki + 2]) - 1)
        places.append(p)
    print(reconstruct(strings, places))
