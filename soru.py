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
inp = input().strip()
while (inp != "" and inp != "\n"):
    pyramid.append([int(x) for x in inp.split()])
    inp = input().strip()
    N+=1

for i in range(len(pyramid)):   
    for x in range(N-i-1):
        pyramid[i].append(0)
for p in pyramid:
    print(p)

def findPathSum(pyr, m, n):
    path = ""
    for i in range(m-1, -1, -1):
        for j in range(i+1):
            if (pyr[i+1][j] > pyr[i+1][j+1]) and not isPrime(pyr[i+1][j]):
                pyr[i][j] += pyr[i+1][j]
            elif not isPrime(pyr[i+1][j+1]):
                pyr[i][j] += pyr[i+1][j+1]

    return pyr[0][0]
print(findPathSum(pyramid, len(pyramid)-1, len(pyramid)-1))







    

   


