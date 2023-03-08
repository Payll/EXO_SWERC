import random
import Exo2
from math import gcd

def InputGenerator():
    for i in range(1, 7):
        with open('IN/EX2/in' + str(i), 'w') as f:
            # un entier aléatoire entre 1 et 12
            f.write(str(10**5) + '\n')
            for j in range(10**5):
                f.write(str(random.randint(1, 12)) + '\n')


def OutputGenerator():
    for i in range(1, 7):
        exo = "EXO2"
        
        with open(exo + '/Secret_Sample/' + str(i) +".in", 'r') as f:
            with open(exo + '/Secret_Sample/' + str(i)+".ans", 'w') as g:
                print("je genere fort la ")
                
                g.write(Exo2.solve(f.read()))            

if __name__ == "__main__":
    OutputGenerator()