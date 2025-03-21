# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:14:22 2025

@author: Mokwena Phemelo
@student no.: 2023129683
"""

## Functions
def g1(x):
    return x - x**3 - 4*x**2 + 10
def g2(x):
    return (10/x - 4*x)**0.5
def g3(x):
    return 0.5*(10 -x**3)**0.5
def g4(x):
    return (10/(4 + x))**0.5
def g5(x):
    return x - (x**3 + 4*x**2 - 10)/(3*x**2 + 8*x)

def FixedPointIteration(g, TOL, p_0,N_0):
    i = 1
    while(i<N_0):
        print(p_0)
        p = g(p_0)
        if(abs(p-p_0) < TOL):
            print(p)
            break
        i+=1
        p_0 = p
        
N_0 = 30
TOL = 1e-9
p_0 = 1.5

a = FixedPointIteration(g4, TOL, p_0, N_0)