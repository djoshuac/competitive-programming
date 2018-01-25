#!/bin/python3
def increment(num):
    index = -1
    num[index] += 1
    while num[index] == 10:
        num[index] = 0
        index -= 1
        num[index] += 1
    return index

def next_lucky(x):
    ticket = list(map(int, x))

    increment(ticket)
    left = sum(ticket[:3])
    right = sum(ticket[3:])

    while left != right:
        # print(left, right, "".join(map(str, ticket)))
        # input()
        index = increment(ticket)
        if index == -1:
            right += 1
        elif index == -2:
            right -= 8
        elif index == -3:
            right -= 17
        elif index == -4:
            right -= 27
            left += 1
        elif index == -5:
            right -= 27
            left -= 8
        elif index == -6:
            right -= 27
            left -= 17

    return "".join(map(str, ticket))

if __name__ == "__main__":
    print(next_lucky(input().strip()))
