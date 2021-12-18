p= int(input("General parameter p: "))
g= int(input("General parameter g: "))
x = int(input("Subscriber A, enter the secret key: "))
if 1 < x < p - 1:
    print("The secret key is correct!")


def FDTB(number) -> object:  # Dec to bin
    StringBNr = str(bin(number))  
    ReverseBNr = (StringBNr[2:])[::-1]  
    return ReverseBNr


binX = FDTB(x)


def EXPV(m,d,N):
    e=1
    for i in range((len(d) - 1), -1, -1):

            e = (e * e) % N
            if d[i] == '1':
                e = (e * m) % N
    return e


y = EXPV(g, binX, p)
print("The public key is calculated!")
m = (input("Subscriber A, enter a message: "))
h = 3
if 1 < h < p:
    print ("Hesh is done!")
binH = FDTB(h)
k = int(input("Subscriber A, enter the number k that is mutually prime with p - 1 : "))
if 1 < k < p-1:
    print("The number k is correct!")
binK = FDTB(k)

r = EXPV(g, binK, p)
print("Value r: " + str(r))
binR = FDTB(r)
u = (h - x * r) % (p-1)


def EvclidAlg(p, k):
    u = [p - 1, 0]
    v = [k, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1]]
        u = v
        v = t
    return u


ResA = EvclidAlg(p, k)
invK = ResA[1]
if invK < 0:
    invK = invK + (p - 1)
if (k * invK) % (p - 1) == 1:
    print("The found inversion value is correct!")
print("Inversion value k: " + str(invK))
print("Calculate value s...")
s = (invK * u) % (p - 1)
print("The value s is calculated: " + str(s))
binS = FDTB(s)
PCh1 = EXPV(y, binR, p)
PCh2 = EXPV(r, binS, p)
PCh = (PCh1 * PCh2) % p
lCh = EXPV(g, binH, p)
if PCh == lCh:
    print("The digital signature is authentic!")
input('Press "Enter" to close the program')
