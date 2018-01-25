def pans_to_bits(pancakes):
    n = 0
    two = 1
    for p in pancakes:
        if p == "-":
            n += two
        two <<= 1
    return n

def flip(bits, i, k):
    flipper = 2**k - 1
    flipper <<= i
    return bits ^ flipper

def answer(bits, k):
    bits = flip(bits, 0, k)
    bits = flip(bits, 4, k)
    bits = flip(bits, 5, k)
    print(bits)
    
if __name__ == "__main__":
    for _ in range(int(input())):
        pans, k = input().split()
        print(answer(pans_to_bits(pans), int(k)))
