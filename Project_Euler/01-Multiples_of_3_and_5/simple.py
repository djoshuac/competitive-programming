def sum_multiples_of_3_and_5_under(n):
    s = 0
    for i in range(3, n, 3):
        s += i
    for i in range(5, n, 5):
        s += i
    for i in range(15, n, 15):
        s -= i
    return s

if  __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(sum_multiples_of_3_and_5_under(n))
