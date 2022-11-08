import math

def calcular_delta(a,b,c):
    return (b**2)-4*a*c

def calcular_x1(a,b,delta):
    return (-1*b + math.sqrt(delta))/(2*a)

def calcular_x2(a,b,delta):
    return (-1*b - math.sqrt(delta))/(2*a)


a = float(input('digite o valor de a:'))
b = float(input(' digite o valor de b:'))
c = float(input(' digite o valor de c'))

delta = calcular_delta(a,b,c)
x1 = calcular_x1(a, b, delta)
x2 = calcular_x2(a, b, delta)
print(delta)
print(x1)
print(x2)


# import math

# def somar (a,b): 
#     return a + b

# def subtrair(a,b):
#     return a - b

# def multiplicar(a,b):
#     return a * b

# def dividir(a,b):
#     return a/b

# def potencia(a,b):
#     return a**b

# def raiz_quadrada(a):
#     return math.sqrt(a)

# a = float(input('digite o valor de a:'))
# b = float(input(' digite o valor de b:'))
# print(a+b)

# print(somar(10, 20))
# print(subtrair(30, 10))
# print(multiplicar(30, 10))
# print(dividir(30, 10))
# print(potencia(2,2))
# print(raiz_quadrada(9))