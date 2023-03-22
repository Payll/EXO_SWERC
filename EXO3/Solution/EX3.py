import sys

file = sys.stdin.read()
lines = file.splitlines()

n = int(lines[0])
k = int(lines[1])
x = int(lines[2])

table = [[-1 for x in range(n + 1)] for y in range(k + 1)]
table[0][0] = 1


def P(k, x):
    if table[k][x] != -1:
        return table[k][x]
    else:
        ret = 0
        if x == 0 or x > k:
            ret = 0
        elif x == 1:
            ret = 1 / n
        else:
            for i in range(0, k):
                ret += (1 / (n - (k - 1 - i)) * P(k - i - 1, x - 1))
        table[k][x] = ret
        return ret


print(P(k, x))
