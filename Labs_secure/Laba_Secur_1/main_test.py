import math
import numpy

with open('block.txt', 'r') as file:
    str_block = file.read().splitlines()
    print('Your C; ', str_block)

block = [int(item) for item in str_block]
print('Your text block: ', block)


a = float
n = int
w = float

def check_sqrt(n):
    a = int(round(math.sqrt(n)) + 1)
    print('Изначальное a: ', a)
    w = 0.1
    while w.is_integer() != True:
        t = pow(a, 2)
        print('Квадраты чисел: ', t)
        w = t - n
        print('Разность нового числа и модуля N: ', w)
        w = math.sqrt(w)
        print('Проверка целочисленности корня: ', w)
        a = a + 1
    print(a-1)
    return a-1, w

def phi(exp):
    p = int(a+w)
    print('P равно: ', p)
    q = int(a-w)
    print('Q равно: ', q)
    res = int((p-1)*(q-1)) #Phi(n)
    print('Произведение p q: ', res)
    d = pow(exp, -1, res)
    print('D равно: ', d)
    return int(d)

def word(d,c):
    total_word = pow(c,d,n)
    return total_word

n = 64806601923671 #int(input('Введите ваш модуль N: '))
print('Ваш модуль: ', n)
exp = 3676721 #int(input('Введите вашу экспоненту exp: '))
print('Ваша экспонента: ', exp)

total = check_sqrt(n)
a = total[0]
w = total[1]

d = phi(exp)

block_total = []
for x in range(len(block)):
    block_total = word(d, block[x])
    print(x+1, '-ый блок', block_total)











