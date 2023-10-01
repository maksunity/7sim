import os
import math
#import numpy
import sys
import mpmath
from decimal import *

with open('block_1.txt', 'r') as file:
    str_block_1 = file.read().splitlines()
    print('Your first block: ', str_block_1)

with open('block_2.txt', 'r') as file:
    str_block_2 = file.read().splitlines()
    print('Your second block: ', str_block_2)

with open('exp.txt', 'r') as file:
    str_exp = file.read().splitlines()
    print('Your exp: ', str_exp)

exp=[int(item) for item in str_exp]

with open('n.txt', 'r') as file:
    str_n = file.read().splitlines()
    print('Your modul N: ', str_n)

def str_to_int(str_block_1, str_block_2, str_n):
    sum_block_1 = str()
    sum_block_2 = str()
    for x in range(len(str_block_1)):
        sum_block_1 = sum_block_1 + str_block_1[x]
    for x in range(len(str_block_2)):
        sum_block_2 = sum_block_2 + str_block_2[x]
    block_1 = int(sum_block_1)
    block_2 = int(sum_block_2)
    print('Int block 1: ', block_1)
    print('Int block 2: ', block_2)
    sum_n = str()
    for x in range(len(str_n)):
        sum_n = sum_n + str_n[x]
    n = int(sum_n)
    print('Int N: ', n)
    return block_1, block_2, n

def power(block_1, block_2, n, r, s):
    new_block_1 = pow(block_1, r, n)
    new_block_2 = pow(block_2, (-s), n)
    print('Power block 1: ', new_block_1)
    print('Power block 2: ', new_block_2)
    return new_block_1, new_block_2

def find_rs(e1, e2):
    gcd, r, s = extended_gcd(e1, e2)
    if gcd != 1:
        return None
    else:
        return abs(r), abs(s)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

e1 = exp[0]
e2 = exp[1]
result = find_rs(e1, e2)

if result:
    r, s = result
    print(f"r = {r},s = {s}")
else:
    print("Нет решений")

mpmath.mp.dps = 400

total = str_to_int(str_block_1,str_block_2, str_n)

block_1 = total[0]
block_2 = total[1]
n = total[2]

new_block = power(block_1, block_2, n, r, s)

block_1 = new_block[0]
block_2 = new_block[1]

multi_e_r_s = e1*r - e2*s

multi = (block_1*block_2)
print('Multiply c1 c2: ', multi)

ans = multi % n
print('Secret code:    ', ans)

with open('total.txt', 'w') as file:
    file.write(str(ans))



