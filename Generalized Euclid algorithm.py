a = int(input("Please Enter positive number a: "))  
b = int(input("Please Enter positive number b (a>b): "))  


def ObobshchennyjAlgorithmEvlkida(a, b):
    u = [a, 1, 0]
    v = [b, 0, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u = v
        v = t
    return u


result = ObobshchennyjAlgorithmEvlkida(a, b)
gcdAB = result[0]
x = result[1]
y = result[2]
print("The found common divisor of a and b : " + str(gcdAB))
print("Found value  x: " + str(x))
print("Found value  y: " + str(y))
input('Press "Enter" to close the program')

