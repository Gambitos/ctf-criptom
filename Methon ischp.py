a= int(input("Enter 1the number a: "))
y= int(input("Enter the number y: "))
p = int(input("Enter the number p: "))
def FDTB(number) -> object:  # Dec to bin
    StringBNr = str(bin(number))
    ReverseBNr = (StringBNr[2:])[::-1]
    return ReverseBNr

def VX(m,c,p): #expfun
    x=1
    for i in range((len(c) - 1), -1, -1):

            x = (x * x) % p
            if (c[i] == '1'):
                x = (x * m) % p
    return x

i = int(0)
k = int(1)
x = int
N2 = int(0)
N3 = int(0)
N5 = int(0)
K = [0]*4
while i != 4:
    binK = FDTB(k)
    x = VX(a,binK,p)
    while x % 2 == 0:
        x = x/2
        N2 = N2 + 1
    while x % 3 == 0:
        x = x / 3
        N3 = N3 + 1
    while x % 5 == 0:
        x = x / 5
        N5 = N5 + 1
    if x == 1:
        print( str(i + 1) + " a smooth number is decomposed into: " + str(N2)+"-Twos "+ str(N3)+ "-Tripls "+ str(N5)+"-Fives" )
        K[i] = k
        i = i + 1
    N2 = 0
    N3 = 0
    N5 = 0
    k = k + 1
print( "The degrees of smooth numbers are correspondingly equal: "+ str(K[0]) + str(K[1]) + str(K[2]) + str(K[3]))
u1 = int(input("Enter the number u1: "))
u2 = int(input("Enter the number u2: "))
u3 = int(input("Enter the number u3: "))
k = 3
i = 0
while i != 1:
    N2 = 0
    N3 = 0
    N5 = 0
    binK = FDTB(k)
    xv =VX(a, binK, p)
    x = ((y * xv) % p)
    while x % 2 == 0:
        x = x / 2
        N2 = N2 + 1
    while x % 3 == 0:
        x = x / 3
        N3 = N3 + 1
    while x % 5 == 0:
        x = x / 5
        N5 = N5 + 1
    if x != 1:
        print( "x = " + str(((u1 * N2) + (u2 * N3) + (u3 * N5) - k) % (p - 1)))
    input('Press "Enter" to close the program')
