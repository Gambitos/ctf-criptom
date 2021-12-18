m = int(input("Enter value (m): "))  
c = int(input("Please Enter positive number:"))  

def Evclid(m, c):
    u = [m, 0]
    v = [c, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1]]
        u = v
        v = t
    return u

result = Evclid (m, c)
invC = result[1]
if invC < 0:
    invC = invC + m
print("Checking the reverse number...")
if (c*invC) % m == 1:
    print("The found inversion value is correct!")

print("reverse number с: " + str(invC))
input('press "Enter" to close the program')

