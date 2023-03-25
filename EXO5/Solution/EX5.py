import sys

file = open("input").read()
lines = file.splitlines()

n = int(lines[0])
nb = int(lines[1])
k1 = int(lines[1])
k2 = int(lines[2])
x = int(lines[3])

table = [[[-1 for x in range(n + 1)] for y in range(n + 1)] for che in range(2)]
table[0][0][0] = 1
table[1][0][0] = 1


def P(n, k, x, che):
    if table[che][k][x] != -1:
        return table[che][k][x]
    else:
        ret = 0
        if x == 0 or x > k:
            ret = 0
        elif x == 1:
            ret = 1 / n
        else:
            for i in range(0, k):
                ret += (1 / (n - (k - 1 - i)) * P(n, k - i - 1, x - 1, che))
        table[che][k][x] = ret
        return ret


proba = 0
for i in range(1, x):
    proba -= P(n - k2, n - k2, i, 1)
proba += 1
proba *= P(n - k1, n - k1, x, 0)
print(proba)
