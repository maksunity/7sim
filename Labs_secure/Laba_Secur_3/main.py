import numpy
import math
import os
import sys
from decimal import Decimal, getcontext

with open('block_1.txt', 'r') as file:
    str_block_1 = file.read().splitlines()
    print('Your C1; ', str_block_1)

with open('block_2.txt', 'r') as file:
    str_block_2 = file.read().splitlines()
    print('Your C2: ', str_block_2)

with open('exp.txt', 'r') as file:
    str_exp = file.read().splitlines()
    print('Your exp: ', str_exp)

with open('n.txt', 'r') as file:
    n = int(file.read())
    print('Yor N: ', n)

block_1=[int(item) for item in str_block_1]
block_2=[int(item) for item in str_block_2]
exp=[int(item) for item in str_exp]

print(block_1)
print(block_2)
print(exp)

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

for x in range(len(block_1)):
    block_1[x] = pow(block_1[x], r, n)
    block_2[x] = pow(block_2[x], (-s), n)

print(block_1)
print(block_2)

m = [0] * len(block_1)
getcontext().prec = 10

for x in range(len(block_1)):
    m[x] = block_1[x] * block_2[x]
    #m[x] = math.fmod(m[x], n)

for x in range(len(m)):
    m[x] = m[x] % n
print('Total array: ', m)

with open('total.txt', 'w') as file:
    for x in range(len(m)):
        file.write(str(m[x]) + '\n')