P= int(input("Subscriber B, enter a prime number P:"))
Q= int(input("Subscriber B, enter a prime number Q:"))
NB = P*Q
ф = (P-1) * (Q-1)
print("The number ф has been calculated successfully:"+ str(ф))
dB = int(input("Choose a number d that is mutually prime with ф (d<ф):"))

def EvclidAlg(ф, d):
    u = [ф, 0]
    v = [d, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1]]
        u = v
        v = t
    return u

result = EvclidAlg(ф, dB)
cB = result[1]
if cB < 0:
    cB = cB + ф
if (cB*dB) % ф == 1:
    print("The found inversion value is correct!")

print("Inversion value db (cb): " + str(cB))


def FDTB(number) -> object:  # Dec to bin
    StringBNr = str(bin(number))  
    ReverseBNr = (StringBNr[2:])[::-1]  
    return ReverseBNr


binDB = FDTB(dB)
binCB = FDTB(cB)
m = int(input("Subscriber A, enter a message to B (m; m<Nb): "))
print("The subscriber encrypts the message...")


def ExpV(m,d,N):
    e=1
    for i in range((len(d) - 1), -1, -1):  #exp func

            e = (e * e) % N
            if d[i] == '1':
                e = (e * m) % N
    return e


e = ExpV(m, binDB, NB)
mRash = ExpV(e, binCB, NB)
print("The message has been decrypted:" + str(mRash))
if mRash == m:
    print("The message received by subscriber B is identical to the original message!")
input('Press "Enter" to close the program')
