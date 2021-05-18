from sympy import *
import math

def der1(eq, x):
    return N(str(diff(eq)).replace('x', str(x)))

def F(eq, x):
    return N(eq.replace('x', str(x)))

def newtons_method(eq, a, b):
    try:
        x0 = (a + b) / 2
        xn = F(eq, x0)
        xn1 = xn - F(eq, xn) / der1(eq, xn)

        while abs(xn1 - xn) > math.pow(10, -5):
            xn = xn1
            xn1 = xn - F(eq, xn) / der1(eq, xn)
        return xn1

    except ValueError:
        print ("Value not invalidate")

if __name__ == '__main__':
    eq = input('Введіть ліву частину рівняння:\n')
    left = int(input('Введіть а:\n'))
    right = int(input('Введіть b:\n'))

    print(f'Розв\'язуємо {eq} = 0\nна проміжку [{left}; {right}]')

    ans = newtons_method(eq, left, right)
    print(f'x = {ans}')

    input()

