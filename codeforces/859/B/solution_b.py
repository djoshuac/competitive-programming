def approach_sum_squares(n):
    i = 1
    s = 1
    for d in range(3, n, 2):
        s += d
        if s > n:
            break
        i += 1
    return i

def min_perim(n):
    k = approach_sum_squares(n)
    n -= k*k
    picks = 4 * k
    if n == 0:
        return picks
    if n <= k:
        return picks + 2
    if n > k:
        return picks + 4

if __name__ == "__main__":
    n = int(input().strip())
    print(min_perim(n))
