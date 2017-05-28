'''
The `change` array is a list of ways to make change
where change[n] is a dictionary of the number of ways to make change for n.

The change[n] dictionary's keys are coins
and the values are the number of ways to make change for n with the key being the largest coin used.

This way all future n can use the previous change[n] dictionaries to figure out
how many ways it can make change for n using a dynamic programming strategy.
'''
def answer(n, coins):
    change = [{0: 1}]
    for i in range(1, n+1):
        change.append({})
        for c in (c for c in coins if c <= i):
            change[i][c] = 0
            for d in range(c+1):
                if d in change[i - c]:
                    change[i][c] += change[i - c][d]
    return sum(change[-1].values())

if __name__ == "__main__":
    n = int(input().split()[0])
    coins = map(int, input().split())
    print(answer(n, sorted(coins)))