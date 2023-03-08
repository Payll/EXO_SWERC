import random
from math import gcd

def InputGenerator():
    for i in range(1, 7):
        with open('IN/EX2/in' + str(i), 'w') as f:
            # un entier aléatoire entre 1 et 12
            f.write(str(10**5) + '\n')
            for j in range(10**5):
                f.write(str(random.randint(1, 12)) + '\n')

def resoudre(n):
    return ""


def OutputGenerator():
    for i in range(1, 7):
        with open('IN/EX2/in' + str(i), 'r') as f:
            with open('OUT/EX2/out' + str(i), 'w') as g:
                # on lit le fichier d'entrée
                n = int(f.readline())
                # on écrit la réponse
                g.write(str(n) + '\n')