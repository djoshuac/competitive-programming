from solution import next_lucky

def test_lucky(param1, exp):
    got = next_lucky(param1)
    if got != exp:
        print("Failed for param1=", param1, "  exp=", exp, "  but got=", got)

if __name__ == "__main__":
    test_lucky("555555", "555564")
    test_lucky("100000", "100001")
