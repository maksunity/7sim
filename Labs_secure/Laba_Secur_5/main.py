import os
import math
import numpy
import sys
import mpmath
from decimal import *

with open('block.txt', 'r') as file:
    str_block = file.read().splitlines()
    print('Your C: ', str_block)

with open('n.txt', 'r') as file:
    str_n = file.read().splitlines()
    print('Your N: ', str_n)

with open('exp.txt', 'r') as file:
    str_exp = file.read()
    exp = int(str_exp)
    print('Your exp: ', exp)

def str_to_int(str_block, str_n):
    sum_block = str()
    for x in range(len(str_block)):
        sum_block = sum_block + str_block[x]
    print('New block: ', sum_block)
    block = int(sum_block)

    sum_n = str()
    for x in range(len(str_n)):
        sum_n = sum_n + str_n[x]
    print('New N: ', sum_n)
    n = int(sum_n)
    return block, n

mpmath.mp.dps = 100

def check_sqrt(n):
    #print('Check N: ', n)
    n_mpf = mpmath.mpf(n)
    a = mpmath.sqrt(n_mpf) + 1
    print('Изначальное a: ', a)
    w = 0.1
    while w != mpmath.nint(w) :
        t = mpmath.power(a,2)
        print('Квадраты чисел: ', t)
        w = t - n_mpf
        print('Разность нового числа и модуля N: ', w)
        w = mpmath.sqrt(w)
        print('Проверка целочисленности корня: ', w)
        a += 1
    print("T = ", a-1)
    return a-1, w

def phi(exp):
    p = a + w  # Extract real parts and round to the nearest integer
    print('P равно: ', p)
    q = a - w
    print('Q равно: ', q)
    res = (p-1)*(q-1) #Phi(n)
    print('Произведение p q: ', res)
    d = mpmath.power(exp, -1)
    print('D равно: ', d)
    return int(d)

def word(block,d,n):
    total_word = pow(block,d,n)
    print('Расшифрованный блок: ', total_word)
    return total_word

block, n = str_to_int(str_block, str_n)

total = check_sqrt(n)

a = total[0]
w = total[1]
d = phi(exp)
word(d,block,n)
