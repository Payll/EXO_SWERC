#! /usr/bin/python3

import os
import sys
import time
from sys import stdin, stdout
import math
# algo





def getProba(n, c, proba):


    #print (str(k) + " " + str(x))

    if c<0 or n<0:
        return 0
    if proba[c][n]!=-1:
        return proba[c][n]
    if n==0 and c==0:
        proba[0][0]=1
        return 1
    p= 1/2*getProba(n-1, c-1, proba) + 1/2*getProba(n-2, c-1, proba)
    #print (str(k) + " " + str(x))
    proba[c][n]=p
    return p




def solve(n, c):
    proba=[]
    for i in range (c+2):
        proba.append([-1]*(n+2))
    p0=getProba(n, c, proba)
    p1=getProba(n+1, c, proba)
    p=p0+p1

    return p





def solve2(n, c):

    p=n-c
    probabilite=0

    if (c-p>=0 and p>=0):
        probabilite+=(math.factorial(c)//math.factorial(c-p)//math.factorial(p)) / 2**c

    p+=1
    if (c-p>=0 and p>=0):
        probabilite+=(math.factorial(c)//math.factorial(c-p)//math.factorial(p)) / 2**c


    return probabilite





# Parsing de l entree Cudoviste
def solveInput(inputStream):

    n, c = tuple(map(int,inputStream.readline().strip().split()))

    res=solve(n, c)
    #res2=solve2(n, c)
    #print (str(res) + " vs " + str(res2))
    return str(res)


# Test2
def test():
    inner_start_time = time.time()

    for c in range (10):
        for n in range (10):
            res=solve(n, c)
            res2=solve2(n, c)
            print ("c=" + str(c) + " n=" + str(n) + "  res=" + str(res) + " vs res2=" + str(res2))


    inner_time = time.time() - inner_start_time
    print(inner_time, "seconde")


# diff
def diff(reponse, attendu, fPrint):
    linesRep = reponse.splitlines()
    linesAtt = attendu.splitlines()

    minLen = min(len(linesRep), len(linesAtt))
    print('Reponse vs Attendu')
    i = 0
    different=False
    while i < minLen:
        res = linesRep[i].strip()
        att = linesAtt[i].strip()
        d=math.fabs(float(res)-float(att))
        if not d<0.000001 :
            different=True
            if fPrint:
                print("=> [" + res + '] [' + att + ']')
            else:
                return True
        else:
            if fPrint:
                print("   [" + res + '] [' + att + ']')
        i = i + 1
    return different


# Juge
if len(sys.argv) >= 2 and sys.argv[1] == 'SAMPLE':
    sampleFolder = "../Secret_Sample/"
    files = os.listdir(sampleFolder)
    reussi = 0
    nbCasDeTest = 0
    for file in files:
        if ".in" in file:
            outputFile = sampleFolder + file.replace(".in", ".out")
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

            check=not diff(res, attendu, False)

            if check:
                print(file.split(".")[0], "success", inner_time, "seconde")
                reussi = reussi + 1
            else:
                print("Erreur avec l'input : ", sampleFolder + file, inner_time, "seconde" )
                diff(res, attendu, True)
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
