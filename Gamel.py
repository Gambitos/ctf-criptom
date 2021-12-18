q = int(input("enter a prime number q:"))
p = 2 * q + 1    
g = int(input("Enter the base value (g):"))
if (1 < g < p - 1 and (g ** q) % p != 1):
    print("Base value is correct")

m = int(input("Subscriber A, enter a message (m; m<p): "))
k = int(input("Subscriber A, enter k: "))
if 1 <= k <= p-2:
    print("k value is correct")


def FDTB(number) -> object:  
    StringBNr = str(bin(number))  
    ReverseBNr = (StringBNr[2:])[::-1]  
    return ReverseBNr


cB=int(input("Subscriber B, enter the secret number (cb):"))

def SecP(c):
    if 1 < c < p-1:
        print("The value of the secret number is correct")
    return

SecP(cB)
binCB = FDTB(cB)

def EXPV(g,k,p):
    r=1
    for i in range((len(k) - 1), -1, -1):  

            r = (r * r) % p
            if k[i] == '1':
                r = (r * g) % p
    return r

print("Process open value...")
dB = EXPV(g, binCB, p)
print("Value db: " + str(dB))
p
binK = FDTB(k)
r = EXPV(g, binK, p)

e1 = m % p
e2 = (dB ** k) % p
e = (e1 * e2) % p
print("Value r: " + str(r) + "Value e: " + str(e))
mRash1 = e % p
mRash2 = (r ** (p-1 - cB)) % p

mRash = (mRash1 * mRash2) % p
print("The message has been decrypted :" + str(mRash))
if mRash == m:
    print("The message received by subscriber B is identical to the original message!")
input('Press "Enter" to close the program')
