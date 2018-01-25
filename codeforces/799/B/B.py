def solution(prices, front, back, cust):
    sold = []
    for c in cust:
        shirt = -1
        price = 1000000001
        for i in range(len(prices)):
            if front[i] == c or back[i] == c:
                if prices[i] < price:
                    shirt = i
                    price = prices[i]
                elif prices[i] == price:
                    shirt = -1
                    price = prices[i]
        if shirt != -1:
            front[shirt] = -1
            back[shirt] = -1
            sold.append(price)
        else:
            sold.append(-1)
    return map(str, sold)

if __name__ == "__main__":
    input()
    prices = list(map(int, input().split()))
    front = list(map(int, input().split()))
    back = list(map(int, input().split()))
    input()
    cust = list(map(int, input().split()))
    print(" ".join(solution(prices, front, back, cust)))
