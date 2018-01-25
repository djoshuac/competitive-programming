if __name__ == "__main__":
    input()
    words = input().split()

    m = max(
        sum(map(lambda a: 1 if a.isupper() else 0, w))
        for w in words
    )
    print(m)
