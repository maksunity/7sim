import os
import math

with open('block_1.txt', 'r') as file:
    block_1 = file.read().splitlines()
    print('Your first block: ', block_1)

with open('block_2.txt', 'r') as file:
    block_2 = file.read().splitlines()
    print('Your second block: ', block_2)

with open('block_3.txt', 'r') as file:
    block_3 = file.read().splitlines()
    print('Your third block: ', block_3)

with open('n.txt', 'r') as file:
    n = file.read().splitlines()
    print('Your moduls: ', n)

int_block_1=[int(item) for item in block_1]
int_block_2=[int(item) for item in block_2]
int_block_3=[int(item) for item in block_3]
int_n=[int(item) for item in n]

print(int_block_1)
print(int_block_2)
print(int_block_3)
print(int_n)

m = [0] * len(int_block_1)
m_0 = [0] * len(int_n)
m_1 = [0] * len(int_n)
m_2 = [0] * len(int_n)
m_3 = [0] * len(int_n)
n_1 = [0] * len(int_block_1)
n_2 = [0] * len(int_block_2)
n_3 = [0] * len(int_block_3)
s = [0] * len(int_block_1)

m_0 = int_n[0] * int_n[1] * int_n[2]
m_1 = int_n[1] * int_n[2]
m_2 = int_n[0] * int_n[2]
m_3 = int_n[0] * int_n[1]

n_1 = pow(m_1, -1, int_n[0])
n_2 = pow(m_2, -1, int_n[1])
n_3 = pow(m_3, -1, int_n[2])


for x in range(len(int_block_1)):
    s[x] = int_block_1[x]*n_1*m_1 + int_block_2[x]*n_2*m_2 + int_block_3[x]*n_3*m_3
    s[x] = s[x] % m_0
    print(s[x])
    m[x] = round(pow(s[x], 1/3), 0)
int_m = [int(items) for items in m]
print(int_m)

with open('Total.txt', 'w') as file:
    for x in range(len(int_m)):
        file.write(str(int_m[x]) + '\n')