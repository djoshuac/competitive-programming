def answer(ar, br):
    br = sorted(br)

    for i, a in enumerate(ar):
        if i > 0:
            if a == 0:
                if br[0] < ar[i - 1]:
                    return "YES"
            elif a < ar[i - 1]:
                return "YES"
        if i < len(ar) - 1 and a == 0:
            if br[-1] > ar[i + 1]:
                print(br[-1], ar[i + 1])
                return "YES"

    return "NO"



def is_increasing(ar):
    last = -1
    for a in ar:
        if a < last:
            return False
        last = a
    return True

if __name__ == "__main__":
    input()
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))
    print(answer(ar, br));
