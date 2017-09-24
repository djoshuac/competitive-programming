biggest = [0];

def is_pandigital_multiple(k, m):
    pan = {'0': True}
    mults = []
    for i in range(1, 10):
        for d in str(m * i):
            if d in pan or int(d) > k:
                return False
            pan[d] = True
        mults.append(m * i)
        if len(pan) - 1 == k:
            test = int("".join(map(str, mults)))
            if test > biggest[0]:
                print(test)
                biggest[0] = test
            return True
    return False


def pandigital_multiples(n, k):
    for m in range(2, n):
        if is_pandigital_multiple(k, m):
            yield m

if __name__ == "__main__":
    n, k = map(int, input().split())
    for result in pandigital_multiples(n, k):
        print(result)
    print(biggest[0])
