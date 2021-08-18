# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:48:20 2021


"""


a=int(input("Enter a number: "))
if a>1:
        for i in range(2,a):
            if a%i==0:
                print(a,"is not a prime number")
                break
            
        else:
            print(a,"is a prime number")