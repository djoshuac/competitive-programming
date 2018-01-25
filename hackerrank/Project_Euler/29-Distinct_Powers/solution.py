def distinct_powers_count(n):
    powers = {}
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            powers[a**b] = True
    return len(powers)

if __name__ == "__main__":
    n = int(input())
    print(distinct_powers_count(n))
