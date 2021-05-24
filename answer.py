import math


def isPrime(n:int)->bool:
    if n==1 or n==0:
        return False
    if n==2:
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

N = 0
pyramid = []
f = open("input.txt")
inp = f.readline()
while (inp != "" and inp != "\n"):
    pyramid.append([0 if isPrime(int(x)) else int(x) for x in inp.split()])
    inp = f.readline()
    N+=1

for i in range(len(pyramid)):   
    for x in range(N-i-1):
        pyramid[i].append(0)

def findPathSum(pyr, m, n):
    temp = pyr.copy()
    
    for i in range(m-2, -1, -1):
        
        for j in range(n):
            if pyr[i][j] == 0:
                continue
            else:
                mx = max(temp[i+1][j],temp[i+1][j+1])
                pyr[i][j] = temp[i][j] + mx

    return pyr[0][0]
print(findPathSum(pyramid, len(pyramid), len(pyramid)))
