def fill(cake, pos1, lowHigh, kid):
    low = (min(pos1[0], lowHigh[0][0],
           min(pos1[1], lowHigh[0][1]))
    high = (max(pos1[0], lowHigh[1][0]),
            max(pos1[1], lowHigh[1][1]))

    for i in range(low[0], high[0]):
        for j in range(low[1], high[1]):
            cake[i][j] = kid

    return (low, high)

def answer(cake):
    kids = {}
    for i, row in enumerate(cake):
        for j, c in enumerate(cake):
            if c != "?":
                if c in kids:
                    kids[c] = fill(cake, (i, j), kids[c]), c)
                else:
                    kids[c] = ((i, j), (i, j))

    col_owners = []
    for j in range(len(cake[0])):
        for i in range(len(cake)):
            if cake[i][j] != "?":
                col_owners.append(cake[i][j])
                break
        if len(col_owners) == j:
            col_owners.append("?")

    for j in range(len(cake[0])):
        owner = col_owners[j]
        for i in range(len(cake)):
            if cake[i][j] == "?" and owner != "?":
                cake[i][j] = owner
            elif j == 0:
                k = cake[i]

    return cake

def print_result(cake, caseNum):
    print("Case " + str(caseNum) + ":")
    for row in cake:
        print("".join(row))

if __name__ == "__main__":
    for caseNum in range(int(input())):
        r, c = map(int, input().split())
        cake = []
        for _ in range(r):
            cake.append(list(input()))
        print_result(answer(cake), caseNum)

