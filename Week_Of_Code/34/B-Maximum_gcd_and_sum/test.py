from solution import maximum_gcd_sum
from brute import maximum_gcd_sum_brute

def test_gcd_and_sum(param1, param2, exp):
    got = maximum_gcd_sum(param1, param2)
    if got != exp:
        print("Failed for param1=", param1, "  param2=", param2, "  exp=", exp, "  but got=", got)

def test_brute(param1, param2, exp):
    got = maximum_gcd_sum_brute(param1, param2)
    if got != exp:
        print("Failed for param1=", param1, "  exp=", exp, "  but got=", got)

import random
import time

def random_test(size):
    return [random.randint(0, 5 * 10**5) for _ in range(size)]

if __name__ == "__main__":
    for i in range(500, 100000, 1000):
        A = random_test(i)
        B = random_test(i)

        t0 = time.time()
        #exp = maximum_gcd_sum_brute(A, B)
        t1 = time.time()
        t_brute = t1 - t0

        t0 = time.time()
        maximum_gcd_sum(A, B)
        #test_gcd_and_sum(A, B, exp)
        t1 = time.time()
        t_solution = t1 - t0

        print(i, t_brute, t_solution)
