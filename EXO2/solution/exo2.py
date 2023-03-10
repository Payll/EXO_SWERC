#! /usr/bin/python3

import os
import sys
import time
from sys import stdin, stdout
import math
# algo





proba=[0]*13
probaStr=["0"]*13
def init():

    proba=[0]*13

    for a in range (1,7):
        for b in range (1,7):
            proba[a+b]+=1

    p=0

    for i in range (2, 13):
        p+=proba[i]
        g=math.gcd(p, 36)
        u=p//g
        v=36//g
        if u==0:
            probaStr[i] = "0"
        elif v==1:
            probaStr[i] = str(u)
        else:
            probaStr[i] = str(u) + "/" + str(v)




def solve(p):
    return probaStr[p]









# Parsing de l entree Cudoviste
def solveInput(inputStream):
    init()
    n = int(inputStream.readline().strip())
    reponses=[]

    for i in range (n):
        p = int(inputStream.readline().strip())
        res=solve(p)
        reponses.append(res)

    return "\n".join(reponses) + "\n"


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
