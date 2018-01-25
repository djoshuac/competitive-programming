if __name__ == "__main__":
    input()
    ar = map(int, input().split())
    m = max(ar)
    if m < 25:
        print(0)
    else:
        print (m - 25)
