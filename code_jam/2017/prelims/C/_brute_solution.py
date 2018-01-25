def answer(n, k):
    stalls = ['0'] + (['.'] * n) + ['0']

    best = (0, 0, 1)

    for _ in range(k):
        best = (-1, -1, -1)
        empty = 0
        for i in range(1, n + 2):
            if stalls[i] == '.':
                empty += 1
            else:
                empty -= 1
                ls = empty // 2
                rs = ls + empty % 2
                
                mn = min(ls, rs)
                mx = max(ls, rs)
                
                if mn > best[0] or mn == best[0] and mx > best[1]:
                    best = (mn, mx, i - rs - 1)
                empty = 0
        stalls[best[2]] = '0'
    return best[1], best[0]

def case_number(i):
    return "Case #" + str(i + 1) + ":"

if __name__ == "__main__":
    for i in range(int(input())):
        n, k = map(int, input().split())
        x, y = answer(n, k)
        print(case_number(i), x, y)
