def meteors(n, ar, br):
    differ = []
    used = {}
    pr = []
    for i in range(n):
        if ar[i] != br[i]:
            pr.append(-1)
            differ.append((i, ar[i], br[i]))
        else:
            pr.append(ar[i])
            used[ar[i]] = i

    unused = find_unused(n, used)

    if len(differ) == 1:
        pr[differ[0][0]] = unused[0]
    elif len(differ) == 2:
        if (not diffs[0][1] in unused) and (not diffs[1][2] in unused):
            pr[diffs[0][0]] = pr[diffs[0][1]]
            pr[diffs[1][0]] = pr[diffs[1][2]]
        else:
            pr[diffs[0][0]] = pr[diffs[0][1]]
            pr[diffs[1][0]] = pr[diffs[1][2]]

    else:
        pr = range(1, n + 1) # bad input

    return pr

def find_unused(n, used):
    unused = []
    for i in range(1, n + 1):
        if not i in used:
            unused.append(i)
    return unused


if __name__ == "__main__":
    n = int(input().strip())
    ar = list(map(int, input().strip().split()))
    br = list(map(int, input().strip().split()))
    print(" ".join(map(str, meteors(n, ar, br))));
