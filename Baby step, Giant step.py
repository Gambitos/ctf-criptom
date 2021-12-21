a = int(input("основание (а): "))
p = int(input("модуль (p): "))
y = int(input("рещение уравнения (y): "))
m = int(input("m: "))
k = int(input("k: "))
if m*k > p:
    print("m и k удовлетворяют условиям")

def FDTB(number) -> object:  
    Strbn = str(bin(number))  
    Rbn = (Strbn[2:])[::-1]  
    return Rbn

def vstep(a,m,p):
    e=1
    for i in range((len(m) - 1), -1, -1):  

            e = (e * e) % p
            if m[i] == '1':
                e = (e * a) % p
    return e

n = [0]*m    
s = [0]*10   

print("вычисляем первый ряд")
j=0
while j<m:
    binM = FDTB(j)
    n1 = vstep(a, binM, p)
    n2 = y % p
    n[j] = (n1 * n2) % p
    j = j + 1

print("первый ряд вычислен" + str(n))

print("вычисляем второй ряд")
i=1

while i < k+1:
        h = i*m
        binH = FDTB(h)                                  
        s[i-1] = vstep(a, binH, p)
        i = i + 1


break_out_flag = False
for j in range(0,len(n)):                
    for i in range(1,len(s)):
        if s[i-1] == n[j]:
            x = i*m - j
            break_out_flag = True
            break
    if break_out_flag:
        break

print("второй ряд вычислен" + str(s))

print("искомый x: " + str(x))

