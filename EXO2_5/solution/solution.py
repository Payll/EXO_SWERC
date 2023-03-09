#n, c = map(int, input().split())

cache = {}

def P(k, x):
    global cache
    if (k, x) in cache:
        return cache[(k, x)]
    if k==0 and x==0:
        return 1
    if k<0 or x<0:
        return 0
    out = (1/2)*P(k-1, x-1) + (1/2)*P(k-2, x-1)
    cache[(k, x)]=out
    return out

def solve(k, c):
    return P(k, c)+P(k+1, c)

#print(solve(int(input()), int(input())))