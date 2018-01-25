def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False;
    return True;

def to_base(n, base):
    num = []
    while n > 0:
        num.append(str(n % base))
        n //= base
    return "".join(reversed(num))

def double_base_palindrome_sum(n, base):
    return sum(i for i in range(n) if is_palindrome(str(i)) and is_palindrome(to_base(i, base)))

if __name__ == "__main__":
    n, base = map(int, input().split())
    print(double_base_palindrome_sum(n, base))
