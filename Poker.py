
p = int(input("Введите значение модуля (p): "))
cА = int(input("Абонент А, введите простое число ca: "))  # Процедура ввода значения cа абонентом А
cB = int(input("Абонент B, введите простое число cb: "))  # Процедура ввода значения cb абонентом B

def FromDecimalToBinary(number) -> object:  # Функция представления десятичного числа в двоичном виде
    StringBinaryNumber = str(bin(number))  # Преобразование десятичного числа в двоичное
    ReverseBinaryNumber = (StringBinaryNumber[2:])[::-1]  # Зеркальная перестановка элементов двоичного числа
    # и отбрасывание первых двух незначащих элементов
    # Например, при преобразовании десятичного числа 2 в двоичное без [2:] вместо 10 выдается результат 0b10
    return ReverseBinaryNumber

def VozvedenieVStepen(a,m,p):
    e=1
    for i in range((len(m) - 1), -1, -1):  # Функция возведения в степень

            e = (e * e) % p
            if m[i] == '1':
                e = (e * a) % p
    return e


def ObobshchennyjAlgorithmEvlkida(p, с):
    u = [p - 1, 0]
    v = [с, 1]
    while v[0] != 0:
        q = u[0] // v[0]
        t = [u[0] % v[0], u[1] - q * v[1]]
        u = v
        v = t
    return u


resultA = ObobshchennyjAlgorithmEvlkida(p, cА)
dA = resultA[1]
if dA < 0:
    dA = dA + (p - 1)
print("Проверка инверсного числа на истинность...")
if (cА * dA) % (p - 1) == 1:
    print("Найденное значение инверсии верное!")

print("Инверсия числа ca (da): " + str(dA))

resultB = ObobshchennyjAlgorithmEvlkida(p, cB)
dB = resultB[1]
if dB < 0:
    dB = dB + (p - 1)
print("Проверка инверсного числа на истинность...")
if (cB * dB) % (p - 1 ) == 1:
    print("Найденное значение инверсии верное!")

print("Инверсия числа cb (db): " + str(dB))

alpha = int(input("Абонент А, выберите случайное число,которое будет соотетствовать первой карте: "))
if 1 < alpha < p - 1 :
    print("Введенное значение удовлетворяет условию!")
betta = int(input("Абонент А, выберите случайное число,которое будет соотетствовать второй карте: "))
if 1 < betta < p - 1 :
    print("Введенное значение удовлетворяет условию!")
gamma = int(input("Абонент А, выберите случайное число,которое будет соотетствовать третьей карте: "))
if 1 < gamma < p - 1 :
    print("Введенное значение удовлетворяет условию!")

print("Пусть числу альфа будет соответствовать тройка")
print("Пусть числу бетта будет соответствовать семерка")
print("Пусть числу гамма будет соответствовать туз")
print("Алиса вычисляет числа u1,u2,u3...")
binCA = FromDecimalToBinary(cА)
u1 = VozvedenieVStepen(alpha, binCA, p)
u2 = VozvedenieVStepen(betta, binCA, p)
u3 = VozvedenieVStepen(gamma, binCA, p)
print("Значения u1,u2,u3 успешно вычислены!")
print("Боб получил три числа и выбрал u2! Отправляет Алисе по линии связи...")
print("Алиса вычисляет число,которое соответствует полученной карте...")
binDA = FromDecimalToBinary(dA)
kartaA = VozvedenieVStepen(u2, binDA, p)

if kartaA == betta:
    print("Алисе досталась карта бетта (семерка)")

print("Боб вычисляет для оставшихся чисел u1,u3 числа v1,v3...")
binCB = FromDecimalToBinary(cB)
v1 = VozvedenieVStepen(u1, binCB, p)
v3 = VozvedenieVStepen(u3, binCB, p)
print("Значения v1,v3 успешно вычислены и отправлены Алисе!")
print("Алиса получила два числа и выбрала v1!Вычисляет w1...")
w1 = VozvedenieVStepen(v1, binDA, p)
print("Алиса вычислила w1 и отправила число обратно Бобу")
print("Боб вычисляет число z,которое соответствует полученной карте...")
binDB = FromDecimalToBinary(dB)
z = VozvedenieVStepen(w1, binDB, p)

print("Бобу досталась карта альфа (тройка)!Карта,оответствующая v2, остается в прикупе")