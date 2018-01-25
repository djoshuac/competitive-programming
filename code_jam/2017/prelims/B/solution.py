def nines(n):
    return "9" * n

def answer(n):
    if len(n) == 1:
        return n

    for c in n:
        if c > n[0]:
            break
        elif c < n[0]:
            if n[0] == '1':
                return nines(len(n) - 1)
            else:
                return str(int(n[0]) - 1) + nines(len(n) - 1)
    
    out = []
    for i in range(0, len(n)-1):
        if n[i] > n[i+1]:                
            out.append(str(int(n[i]) - 1))
            return "".join(out) + nines(len(n) - i - 1)
        else:
            out.append(n[i])
    return "".join(out) + n[-1]

if __name__ == "__main__":
    for i in range(int(input())):
        print("Case #" + str(i + 1) + ":", answer(input()))
