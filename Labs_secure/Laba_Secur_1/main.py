import math
import numpy

a = int
w = float
n = int

with open('block.txt', 'r') as file:
    str_block = file.read().splitlines()
    print('Your C; ', str_block)

block = [int(item) for item in str_block]
print('Your text block: ', block)

def check_sqrt(n):
    a = int(math.sqrt(n)) + 1
    print('Изначальное a: ', a)
    w = 0.1
    while w.is_integer() != True:
        a = a+1
        t = pow(a, 2)
        print('Квадраты чисел: ', t)
        w = t - n
        print('Разность нового числа и модуля N: ', w)
        w = math.sqrt(w)
        print('Проверка целочисленности корня: ', w)
    print(a)
    return a

    def phi(exp, a, w):
        p = a + w
        print('P равно: ', p)
        q = a - w
        print('Q равно: ', q)
        res = (p - 1) * (q - 1)
        d = pow(exp, -1) % res
        print('D равно: ', d)
        return d
        print(d)
        phi(input('Введите экспоненту: ', exp), a, w)


'''
def phi(exp, a, w):
    p = a+w
    print('P равно: ', p)
    q = a-w
    print('Q равно: ', q)
    res = (p-1)*(q-1)
    d = pow(exp, -1) % res
    print('D равно: ', d)
    return d
'''

n = int(input('Введите ваш модуль N: '))
print('Ваш модуль: ', n)
#exp = int(input('Введите вашу экспоненту exp: '))
#print('Ваша экспонента: ', exp)

check_sqrt(n)





