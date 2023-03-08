from solution import solve
import random

FOLDER = "Secret_Sample/"
n = int(input("Nb de tests à générer: "))

for i in range(n):
    k = random.randrange(10, 100)
    c = random.randrange(int(k/2), k-1)
    s = solve(k, c)
    f = open(FOLDER+str(i+11)+".in", "w")
    f.write(str(k)+" "+str(c))
    f.close()
    f = open(FOLDER+str(i+11)+".out", "w")
    f.write(str(s))
    f.close()
    print(k, c, s)