
m = int(input("Subscriber A, enter a message: "))
pA = int(input("Subscriber A, enter a prime number (p): "))
pB = pA
cА = int(input("Subscriber A, enter a prime number ca: "))
cB = int(input("Subscriber A, enter a prime number cb: "))  

def EvclidAlg(p, с):
    u = [p - 1, 0]
    v = [с, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1]]
        u = v
        v = t
    return u

resultA = EvclidAlg(pA, cА)
dA = resultA[1]
if dA < 0:
    dA = dA + (pA - 1)
print("Checking the inverse number...")
if (cА * dA) % (pA - 1 ) == 1:
    print("The found inversion value is correct!")

print("inversion value (da): " + str(dA))

resultB = EvclidAlg(pB, cB)
dB = resultB[1]
if dB < 0:
    dB = dB + (pB - 1)
print("Checking the inverse number...")
if (cB * dB) % (pB - 1) == 1:
    print("The found inversion value is correct!")
print("inversion value cb: " + str(dB))

def FDTB(number) -> object:  # Dec to bin
    StringBNr = str(bin(number))  
    ReverseBNr = (StringBNr[2:])[::-1]  
    return ReverseBNr

binCA = FDTB(cА)

def VX(m,c,p):
    x=1
    for i in range((len(c) - 1), -1, -1):

            x = (x * x) % p
            if (c[i] == '1'):
                x = (x * m) % p
    return x


x1 = VX(m,binCA,pA)
binCB = FDTB(cB)
x2 = VX(x1,binCB,pB)
binDA = FDTB(dA)
x3 = VX(x2,binDA,pA)
binDB = FDTB(dB)
x4 = VX(x3,binDB,pB)
if x4 == m:
    print("The message received by subscriber B is identical to the original message!")
input('Press "Enter" to close the program')
