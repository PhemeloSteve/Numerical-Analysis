# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:14:22 2025

@author: Mokwena Phemelo
@studen
"""
import math as m

def f(x):
    return m.sin(x) - x

p0 = 0.5
p1 = m.pi/4
N0 = 7
TOL = 1e-9

def FalsePosition(f,p0, p1,TOL,N0):
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while(i<=N0):
        
        p = p1 - q1*(p1-p0)/(q1-q0)
        if(abs(p-p1)<TOL):
            print(p)
            break
        print(p)
        i+=1
        q=f(p)
        if(q*q1<0):
            p0 = p1
            q0 = q1
        p1 = p
        q1 = 2
    print(f"Method failed after N0 iterations, N0 = {N0}")

FalsePosition(f,p0, p1,TOL,N0)