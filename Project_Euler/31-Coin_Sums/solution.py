change = [{0: 1}]
coins = [1, 2, 5, 10, 20, 50, 100, 200]
def coin_sums(n):
    for i in range(len(change), n+1):
        change.append({})
        for c in (c for c in coins if c <= i):
            change[i][c] = 0
            for d in range(c+1):
                if d in change[i - c]:
                    change[i][c] += change[i - c][d]
                    change[i][c] %= 1000000007
    return sum(change[n].values()) % 1000000007

if __name__ == "__main__":
    for _ in range(int(input())):
        print(coin_sums(int(input())))
