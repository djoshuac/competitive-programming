def distinct_powers_count(n):
    powers = {}
    for a in range(2, n):
        for b in range(2, n):
            powers[a**b] = True
        print(a)
    return len(powers)
