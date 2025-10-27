import numpy as np
import pandas as pd

df = pd.read_csv('message.csv')
# print(df.head())

H_big = [
    [1,1,0,0,1,1,0,0,0],
    [1,1,1,0,0,0,1,0,0],
    [1,0,1,1,0,0,0,1,0],
    [1,0,0,1,1,0,0,0,1]
    ]
error_to_bit = {
        tuple([1,1,1,1]):0,
        tuple([1,1,0,0]):1,
        tuple([0,1,1,0]):2,
        tuple([0,0,1,1]):3,
        tuple([1,0,0,1]):4,
        tuple([1,0,0,0]):5,
        tuple([0,1,0,0]):6,
        tuple([0,0,1,0]):7,
        tuple([0,0,0,1]):8,
        tuple([0,0,0,0]):-1,
        }
G_big = [
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,1],
    [1,1,1,0,0],
    [1,0,1,1,0],
    [1,0,0,1,1]
    ]

def mod_matmul(arr1, arr2):
    out = [0,0,0,0]
    index = 0
    for row in arr1:
        tmp = 0
        for i in range(len(arr2)):
            tmp = (tmp + arr2[i] * row[i]) % 2
        out[index] = tmp
        index += 1
    return out



checks = []
np_arr = df.to_numpy().tolist()
for row in np_arr:
    new_arr = mod_matmul(H_big, row)
    # print(new_arr)
    checks.append(new_arr)

# print(checks)
bit_errors = [error_to_bit[tuple(check)] for check in checks]

# print(bit_errors)
# print(np_arr)
for i in range(len(checks)):
    row = checks[i]
    if(row != [0,0,0,0]):
        np_arr[i][error_to_bit[tuple(row)]] = np_arr[i][error_to_bit[tuple(row)]] ^ 1
    # print(row)
print(np_arr)

alpha = [
        [0,0,0,0,0],
        [],

        ]

recovered_bits = [bit_string[0:5] for bit_string in np_arr]
print(recovered_bits)

decimal_nums = [int("".join(map(str, recovered)), 2) for recovered in recovered_bits]

decoded = ""
for decimal in decimal_nums:
    if decimal == 0:
        decoded += " "
        continue
    decoded += (chr(decimal + 96))
print(decoded)
