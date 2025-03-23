# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:14:22 2025
@author: Mokwena Phemelo
@studen
"""
import math as m

def f(x):
    return m.cos(x) - x

def f_prime(x):
    return -m.sin(x) - 1

p0 = 0.5
p1 = m.pi/4-0.001
N0 = 7
TOL = 1e-9

def FalsePosition(f,p0, p1,TOL,N0):
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while(i<=N0):
        
        p = p1 - q1*(p1-p0)/(q1-q0)
        print(p0)
        if(abs(p-p1)<TOL):
            print(p)
            break
        i =  i + 1
        q=f(p)
        if(q*q1<0):
            p0 = p1
            q0 = q1
        p1 = p
        q1 = 2
    print(f"Method failed after N0 iterations, N0 = {N0}")

##FalsePosition(f,p0, p1,TOL,N0)

def SecantMethod(f,p0, p1,TOL,N0):
    i = 2
    q0 =f(p0)
    q1 = f(p1)
    while(i<N0):
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        if abs(p - p1) < TOL :
            print(p)
            return p
        i+=1
        p0 = p1
        q0  = q1
        p1 = p
        q1 = f(p)
    print(f"Method failed after {N0-i} iteration, N_0 = ", N0)

##SecantMethod(f,p0, p1,TOL,N0)

def NewtonMetho(p0, TOL,N0):
    i = 1
    while i<N0:
        
        p = p0 - f(p0)/f_prime(p0)
        if abs(p-p0) < TOL:
            print(p)
            return p
        i+=1
        p0 = p
        print(p0)
    print(f"The method failed after {N0 - i} iterations, N_0 = ", N0)

NewtonMetho(p0, TOL,N0)
