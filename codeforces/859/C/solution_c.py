def maximum_pie_consumption(pies):
    c = len(pies) - 1
    toke = wait = 0
    for p in reversed(pies):
        if toke < p + wait:
            toke, wait = wait + p, toke
        else:
            wait += p
    return wait, toke

if __name__ == "__main__":
    input()
    pies = list(map(int, input().strip().split()))
    print(" ".join(map(str, maximum_pie_consumption(pies))))
