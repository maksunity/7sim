import os
import math
import mpmath
from decimal import Decimal, getcontext

with open('block_1.txt', 'r') as file:
    str_block_1 = file.read().splitlines()
    print('Your first block: ', str_block_1)

with open('block_2.txt', 'r') as file:
    str_block_2 = file.read().splitlines()
    print('Your second block: ', str_block_2)

with open('block_3.txt', 'r') as file:
    str_block_3 = file.read().splitlines()
    print('Your third block: ', str_block_3)

with open('n_1.txt', 'r') as file:
    str_n_1 = file.read().splitlines()
    print('Your first module N: ', str_n_1)

with open('n_2.txt', 'r') as file:
    str_n_2 = file.read().splitlines()
    print('Your second module N: ', str_n_2)

with open('n_3.txt', 'r') as file:
    str_n_3 = file.read().splitlines()
    print('Your third module N: ', str_n_3)

def str_to_int():
    sum_block_1 = str()
    sum_block_2 = str()
    sum_block_3 = str()
    for x in range(len(str_block_1)):
        sum_block_1 = sum_block_1 + str_block_1[x]
    for x in range(len(str_block_2)):
        sum_block_2 = sum_block_2 + str_block_2[x]
    for x in range(len(str_block_3)):
        sum_block_3 = sum_block_3 + str_block_3[x]
    block_1 = int(sum_block_1)
    block_2 = int(sum_block_2)
    block_3 = int(sum_block_3)
    print('New block 1: ', block_1)
    print('New block 2: ', block_2)
    print('New block 3: ', block_3)
    sum_n_1 = str()
    sum_n_2 = str()
    sum_n_3 = str()
    for x in range(len(str_n_1)):
        sum_n_1 = sum_n_1 + str_n_1[x]
    for x in range(len(str_n_2)):
        sum_n_2 = sum_n_2 + str_n_2[x]
    for x in range(len(str_n_3)):
        sum_n_3 = sum_n_3 + str_n_3[x]
    n_1 = int(sum_n_1)
    n_2 = int(sum_n_2)
    n_3 = int(sum_n_3)
    print('New N_1: ', n_1)
    print('New N_2: ', n_2)
    print('New N_3: ', n_3)
    return block_1, block_2, block_3, n_1, n_2, n_3

total = str_to_int()

c_1 = total[0]
c_2 = total[1]
c_3 = total[2]
n_1 = total[3]
n_2 = total[4]
n_3 = total[5]

m_0 = n_1 * n_2 * n_3
m_1 = n_2 * n_3
m_2 = n_1 * n_3
m_3 = n_1 * n_2

n_1_new = pow(m_1, -1, n_1)
n_2_new = pow(m_2, -1, n_2)
n_3_new = pow(m_3, -1, n_3)

s = c_1*n_1_new*m_1 + c_2*n_2_new*m_2 + c_3*n_3_new*m_3

print('s = ', s)
print('M0 = ', m_0)

s_total = s % m_0
print('S Mod M0 = ', s_total)
mpmath.mp.dps = 630
check = mpmath.fdiv(1,3)
print(check)
s_total - mpmath.mpf(s_total)
m_total = int(mpmath.power(s_total, check))
print('M = ', m_total)
calc = 29156648940488760127405092842936228683781865773014263203560204681488329625097702592003644773899765686747911320525036298050334796372130362685889714356484526332258785741528241676638959101385741143852243979315638637683546240313419864515133142448177312030258015596848656082746654594325592721453738596578995292801288189791770049505883434346834622373457846025492333363239156473741160680025018183078646108246960634572054761996317380778932121099838595640421851663451625737047343627336158834540914736953730321186598542603978627565251872559177477980102695758114528350282073179670035730703676561136082993789423905002
print('M = ', calc)

with open('total.txt', 'w') as file:
    file.write(str(m_total))

diff = m_total/calc
print('Different: ', diff)