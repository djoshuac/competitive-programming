def maximum_expected_bracket(prob):
    pass

if __name__ == "__main__":
    n = int(input().strip())
    prob = [
        list(map(int, input().split().strip()))
        for _ in range(n)
    ]
    result = maximum_expected_bracket(prob)
