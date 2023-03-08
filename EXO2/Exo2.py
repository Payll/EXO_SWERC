import random
def solve(lines) :

    res = ""
    for l in lines.splitlines()[1:] :
        vals = {1:"0", 2:"1/36",3:"1/12",4:"1/6",5:"5/18",6:"5/12",7:"7/12",8:"13/18",9:"5/6",10:"11/12",11:"35/36",12:"1"}
        res += str(vals[int(l)]) +"\n" 

    return res 

def GenerateInput():
    for i in range(7):
        with open('EXO2/Secret_Sample/' + str(i) + ".in", 'w') as f:
            # un entier aléatoire entre 1 et 12
            f.write(str(10**5) + '\n')
            for j in range(10**5):
                f.write(str(random.randint(1, 12)) + '\n')


def GenerateOutputs():

    for i in range(7):
        with open('EXO2/Secret_Sample/' + str(i) +".in", 'r') as f:
            with open('EXO2/Secret_Sample/' + str(i)+".ans", 'w') as g:
                g.write(solve(f.read()))   