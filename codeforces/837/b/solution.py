def check_row(color, row):
    for f in row:
        if f != color:
            return False
    return True


def solution(flag, n, m, tpose):
    if n % 3 != 0 and not tpose:
        if tpose:
            return "NO"
        return solution(transpose(flag), m, n, True)

    colors = [
        flag[0][0],
        flag[n // 3][0],
        flag[n // 3 * 2][0]
    ]

    if check_row(colors[0], colors):
        if tpose:
            return "NO"
        return solution(transpose(flag), m, n, True)

    if not check_row(colors[0], flag[0]) and not tpose:
        if tpose:
            return "NO"
        return solution(transpose(flag), m, n, True)

    for c, color in enumerate(colors):
        for i in range(n // 3 * c, n // 3 * (c + 1)):
            if not check_row(color, flag[i]):
                return "NO"
    return "YES"



def transpose(flag):
    pose = []
    for i in range(len(flag[0])):
        pose.append([])
        for j in range(len(flag)):
            pose[i].append(flag[j][i])
    return pose

if __name__ == "__main__":
    n, m = map(int, input().split())
    flag = [
        input()
        for _ in range(n)
    ]
    print(solution(flag, n, m, False))
