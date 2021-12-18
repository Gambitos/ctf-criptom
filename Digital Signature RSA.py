P= int(input("Subscriber A, enter a prime number P:"))
Q= int(input("Subscriber A, enter a prime number Q:"))
N = P*Q
ф = (P-1) * (Q-1)
print("The number ф has been calculated successfully: "+ str(ф))
d = int(input("Choose a number d that is mutually prime with ф (d<ф):"))

def EvclidAlg(ф, d):
    u = [ф, 0]
    v = [d, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1]]
        u = v
        v = t
    return u


result = EvclidAlg(ф, d)
c = result[1]
if c < 0:
    c = c + ф
if (c*d) % ф == 1:
    print("The found inversion value is correct!")

print("Inversion value d (c): " + str(c))


def FDTB(number) -> object:  # Dec to bin
    StringBNr = str(bin(number))  
    ReverseBNr = (StringBNr[2:])[::-1]  
    return ReverseBNr


binD = FDTB(d)
binC = FDTB(c)
m = (input("Subscriber A, enter a message: "))
y = 13
print("Hesh is done!")



def ExpV(m,d,N):
    e=1
    for i in range((len(d) - 1), -1, -1):  #exp func

            e = (e * e) % N
            if d[i] == '1':
                e = (e * m) % N
    return e


s = ExpV(y, binC, N)
hesh2 = 13
w = ExpV(s, binD, N)
if hesh2 == w:
    print("The digital signature is authentic: " + str(s))
input('Press "Enter" to close the program')
