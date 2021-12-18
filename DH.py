def FromDecimalToBinary(number) :  #Dec to bin fun
    StringBin = str(bin(number)) #TO bin
    ReverseBin = (StringBin[2:])[::-1]
    return ReverseBin
def Openkeyfun (X,g,p): #Fun openkey
    Y=1
    for i in range((len(X) - 1), -1, -1):# Fun exp
        Y = (Y * Y) % p
        if (X[i] == '1'):
            Y = (Y * g) % p
    return Y
q=int(input("input prime - q:"))
XA=int(input("Абонент А, input open key :"))
binXA= FromDecimalToBinary(XA)
XB=int(input("Абонент B, input secret key :"))
binXB= FromDecimalToBinary(XB)
p= 2*q + 1
g =int(input("Enter (g):"))
YA= Openkeyfun(binXA,g,p)
YB= Openkeyfun(binXB,g,p)
print("Open keys combed")
YA,YB= YB,YA #Обмен открытыми ключами
print("Swap keys successful")

def SecretkeyFun(Y,X,p):
    Z=1
    for i in range((len(X) - 1), -1, -1):  #Функция вычисления общего закрытого ключа

            Z = (Z * Z) % p
            if (X[i] == '1'):
                Z = (Z * Y) % p
    return Z

ZAB = SecretkeyFun(YB,binXA,p)
ZBA = SecretkeyFun(YA,binXB,p)
print("Calculation of the shared secret key is successful!secret key : " + str(ZAB))
input('Press :ENTER:')