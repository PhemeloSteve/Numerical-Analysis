# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:14:22 2025

@author: Mokwena Phemelo
@student no.: 2023129683
"""

import numpy as np

## Functions
def g1(x):
    return x - x**3 - 4*x**2 + 10

def g2(x):
    if x == 0:
        return np.nan  # Handle division by zero
    return (10/x - 4*x)**0.5

def g3(x):
    return 0.5*(10 - x**3)**0.5

def g4(x):
    return (10/(4 + x))**0.5

def g5(x):
    return x - (x**3 + 4*x**2 - 10)/(3*x**2 + 8*x)

def FixedPointIteration(g, TOL, p_0, N_0):
    i = 1
    nums = np.array([p_0])  # Initialize as a NumPy array
    while i < N_0:
        p = g(nums[-1])  # access the last value of the numpy array
        if np.isnan(p):  # check for nan
            return nums  # return what was calculated before nan
        if abs(p - nums[-1]) < TOL:
            nums = np.append(nums, p)  # append to numpy array
            return nums
        i += 1
        nums = np.append(nums, p)
    return nums

N_0 = 30
TOL = 1e-12
p_0 = 1.5

a = FixedPointIteration(g1, TOL, p_0, N_0)
b = FixedPointIteration(g2, TOL, p_0, N_0)
c = FixedPointIteration(g3, TOL, p_0, N_0)
d = FixedPointIteration(g4, TOL, p_0, N_0)
e = FixedPointIteration(g5, TOL, p_0, N_0)

print("------------------------------------------------------------------------------------------------------------------------")
print("n             (a)                     (b)                     (c)                     (d)                     (e)")
print("------------------------------------------------------------------------------------------------------------------------")

# Determine the max length of the returned arrays.
max_length = max(len(a), len(b), len(c), len(d), len(e))

for i in range(max_length): #loop to max length
    a_val = a[i] if i < len(a) else np.nan
    b_val = b[i] if i < len(b) else np.nan
    c_val = c[i] if i < len(c) else np.nan
    d_val = d[i] if i < len(d) else np.nan
    e_val = e[i] if i < len(e) else np.nan
    print(f"{i+1:2}. {a_val:20.10f} {b_val:20.10f} {c_val:20.10f} {d_val:20.10f} {e_val:20.10f}")

    