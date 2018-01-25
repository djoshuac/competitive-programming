from solution import same_occurrances as solution
from brute import same_occurrances as brute

import random

def test(x, y, numbers):
    b = brute(x, y, numbers)
    s = solution(x, y, numbers)

    if b != s:
        print("Failed for x=", x, " y=", y, " numbers=", numbers, " got=", s, " but expected=", b)
        raise "Falied test"

def random_int(x_range):
    return random.randint(x_range[0], x_range[1])

if __name__ == '__main__':
    size_range = (10, 15)
    value_range = (0, 5000)
    query_count = 20

    for _ in range(50):
        print("testing", _)
        numbers = [random_int(value_range) for _ in range(random_int(size_range))]
        for q in range(query_count):
            x, y = random_int(value_range), random_int(value_range)
            test(x, y, numbers)
