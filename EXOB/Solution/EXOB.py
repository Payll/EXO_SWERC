import sys

file = sys.stdin.read()
lines = file.splitlines()

# number of element and number of chemist
n, nb = map(int, lines[0].split())

# list of the starting point of each chemist
k = list(map(int, lines[1].split()))

table = [[[-1 for x in range(n + 1)] for y in range(n + 1)] for che in range(nb)]
for che in range(nb):
    table[che][0][0] = 1


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


output = ""
for che in range(0, nb):
    # Get the probability of winning of the chemist che
    proba = 0
    for x in range(0, n+1):
        # Get the probability of winning of the chemist che with x steps
        proba_x = 1
        for che_i in range(0, nb):
            # Get the probability of winning of the chemist che_i
            if che_i != che:
                proba_che = 0
                for i in range(0, x):
                    proba_che -= P(n - k[che_i], n - k[che_i], i, che_i)
                proba_che += 1
                proba_x *= proba_che
        proba += P(n - k[che], n - k[che], x, che) * proba_x
    output += str(proba) + " "
print(output[:-1])

