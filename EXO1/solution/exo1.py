#! /usr/bin/python3

import os
import sys
import time
from sys import stdin, stdout
import math
# algo


def solveUnit(m, p, a, b):
    if a==b and m!=p:
        return "NO"
    if a==b and m==p:
        return "YES"
    if (m*a-p*b)*(a-b)>=0 and (m*a-p*b)%(a-b)==0 and (m*a-p*b)//(a-b)<=min(m, p):
        return "YES"
    if (m*b-p*a)*(b-a)>=0 and (m*b-p*a)%(b-a)==0 and (m*b-p*a)//(b-a)<=min(m, p):
        return "YES"

    r1 = (m*a-p*b)//(a-b)
    r2 = (m*b-p*a)//(b-a)

    return "NO"




def solve(nbP, nbM, consoles):

    reponses=[]
    for t in consoles:
        res=solveUnit(nbM, nbP, t[0], t[1])
        reponses.append(res)

    return "\n".join(reponses)









# Parsing de l entree Cudoviste
def solveInput(inputStream):
    n = int(inputStream.readline().strip())



    return "Bob a " + str (n) + " chances sur 6 de gagner"


# Test2
def test():
    inner_start_time = time.time()

   
    inner_time = time.time() - inner_start_time
    print(inner_time, "seconde")


# diff
def diff(reponse, attendu):
    linesRep = reponse.splitlines()
    linesAtt = attendu.splitlines()

    minLen = min(len(linesRep), len(linesAtt))
    print('Reponse vs Attendu')
    i = 0
    while i < minLen:
        res = linesRep[i].strip()
        att = linesAtt[i].strip()

        if not res == att:
            print("=> [" + res + '] [' + att + ']')
        else:
            print("   [" + res + '] [' + att + ']')
        i = i + 1


# Juge
if len(sys.argv) >= 2 and sys.argv[1] == 'SAMPLE':
    sampleFolder = "../Secret_Sample/"
    files = os.listdir(sampleFolder)
    reussi = 0
    nbCasDeTest = 0
    for file in files:
        if ".in" in file:
            outputFile = sampleFolder + file.replace(".in", ".ans")
            if not os.path.exists(outputFile):
                continue
            nbCasDeTest += 1
            print("---------------------------")
            print("Cas de test " + file)

            attendu = open(outputFile, "r").read()

            inputStream = open(sampleFolder + file, "r")

            # print("listeInput:" + "".join(listeInput))
            inner_start_time = time.time()

            # lecture du resultat
            res = solveInput(inputStream)

            inner_time = time.time() - inner_start_time

            check = res == attendu
            if check:
                print(file.split(".")[0], "success", inner_time, "seconde")
                reussi = reussi + 1
            else:
                print("Erreur avec l'input : ", sampleFolder + file, inner_time, "seconde" )
                diff(res, attendu)
                print("Obtenu  : [" + res + "]\nAttendu : [" + attendu + "]")
    print("")
    print("--------------BILAN--------------")
    print(str(reussi) + "/" + str(nbCasDeTest))

elif len(sys.argv) >= 2 and sys.argv[1] == 'TEST':
    print("--------------TEST--------------")
    test()
else:
    ret = solveInput(stdin)
    stdout.write(ret)
