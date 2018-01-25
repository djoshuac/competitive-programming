def sum_multiples_of_3_and_5_under(n):
    n -= 1
    s = (n // 3) * (n // 3 + 1) * 3
    s += (n // 5) * (n // 5 + 1) * 5
    s -= (n // 15) * (n // 15 + 1) * 15
    s //= 2
    return s

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(sum_multiples_of_3_and_5_under(n))
