#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:08:07 2021

@author: amedranomdelc
"""

def isSumOf3squares(n):
    if n%2 != 0:
        if n%8 != 7:
            return True
        else:
            return False
    if n%2 == 0:
        n = n//2
        if n%2 != 0:
            return True
        else:
            n = n//2
            return isSumOf3squares(n)
    
def smallestPrime(n):
    if n == 1:
        return None
    i = 2
    while i*i <= n:
        if n%i == 0:
            return i
        else:
            i += 1
    return n

def numSquares(n):
    if not isSumOf3squares(n):
        return 4
    
    primes = {}
    while n > 1:
        p = smallestPrime(n)
        if p in primes:
            primes[p] = primes[p] + 1
        else:
            primes[p] = 1
        n = n//p
    
    gaussian = False
    even = True
    
    for p in primes:
        if p%4 == 2:
            if primes[p]%2 == 1:
                even = False
                gaussian = True
                
        if p%4 == 1:
            gaussian = True
            if primes[p]%2 == 1:
                even = False
            
        if p%4 == 3:
            if primes[p]%2 == 1:
                return 3

    if even:
        return 1
    else:
        if gaussian:
            return 2

n = int(input("Enter a positive integer:"))
if type(n) != int:
    print("Please enter positive integer")
elif n < 0:
    print("Please enter positive integer")
else:
    s = numSquares(n)
    print("Great! The minimal amount of positive squares needed to add up " + str(n) + " is " + str(s))
          