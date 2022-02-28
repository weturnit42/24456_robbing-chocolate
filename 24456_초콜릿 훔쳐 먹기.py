import math

def factorize(n):
    factor = []

    for i in range(1, math.ceil(n ** 0.5)):
        if(n%i == 0):
            factor.append(i)

    #print(factor)
    return factor

N, M, K = map(int, input().split())

choco = N*M
chocoAte = 0
D_old = abs(N-M)
check = True
while(choco>1):
    factor = factorize(int(N*M-1))
    for i in factor:
        D_new = int(abs(i-(N*M-1)/i))
        if(abs(D_old - D_new) <= K):
            M=(N*M-1)/i
            N=i
            choco = N*M
            chocoAte = chocoAte + 1
            break

        if(i == factor[-1]):
            break
    
    D_old = D_new
    if(check == False):
        break

print(chocoAte)
