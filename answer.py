import math
import numpy as np

def isPrime(n:int)->bool:
    if n==1 or n==0:
        return False
    if n==2:
        return True
    for i in range(2,int(math.sqrt(n)+1)+1):
        if n%i == 0:
            return False
    return True

N = 0
pyramid = []
f = open("input.txt")
inp = f.readline()
while (inp != "" and inp != "\n"):
    pyramid.append([-1 if isPrime(int(x)) else int(x) for x in inp.split()])
    inp = f.readline()
    N+=1

for i in range(len(pyramid)):   
    for x in range(N-i-1):
        pyramid[i].append(0)

def findPathSum(pyr, m, n):
    temp = []
    for r in pyr:
        temp.append(r.copy())

    l = 0
    path = []
    path.append(temp[0][0])
    for k in range(m-1):
        
        if  temp[k+1][l+1] > temp[k+1][l]:
            l = l+1
        if temp[k+1][l] != -1:
            path.append(temp[k+1][l])

    print("path: "+str(path))
    return np.sum(path)

print(findPathSum(pyramid, len(pyramid), len(pyramid)))
