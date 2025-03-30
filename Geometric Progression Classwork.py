# OZOKO-EMMANUEL DELIGHT
# 20CJ027488
# COMPUTER ENGINEERING
# CEN 524

#Assingment - A python script for the sum of a GP

import math

def gp_r_less_than_1() -> float: # When r is less than |1|

    formular = 'a(1-r^n)/(1-r)'

    print(f"This is the formula for the GP if r < 1: {formular}")
    
    a = int(input("What is your first number(a): "))
    r = float(input("What is the commin ratio(r): "))
    if r == 1:
        raise ValueError("Commom raise cannot be 1")
    elif r >= 1:
        raise ValueError("Value of 'r' should be less than 1")
        
    n = int(input("How many number of terms(n): "))
    
    result = a*(1-math.pow(r,n))/(1-r)
    
    print(f"The GP is = {result}")

def gp_r_greater_than_1() -> float:

    formular = 'a((r^1)-1)/(r-1)'

    print(f"This is the formula for the GP if r > 1: {formular}")
    
    a = int(input("What is your first number(a): "))
    r = float(input("What is the commin ratio(r): "))
    if r == 1:
        raise ValueError("Commom raise cannot be 1")
    elif r <= 1:
        raise ValueError("Value of 'r' should be greater than 1")
        
    n = int(input("How many number of terms(n): "))
    
    result = a*(math.pow(r,n)-1)/(r-1)
    
    print(f"The GP is = {result}")

def gp_n_is_inf() -> float:

    formular = 'a/(1-r)'
    
    print(f"This is the formula for the GP if n is infinity: {formular}")
    a = int(input("What is your first number(a): "))
    r = float(input("What is the commin ratio(r): "))
    n = int(input("How many number of terms(n): "))
    if n > 10000:
        n = math.inf
    else:
        raise ValueError("The 'n' value is not big enough to be considered as infinity!!\nTry a number above 10000")
    if abs(r) >= 1:
        raise ValueError("Common ratio must be less than 1 in this equation")
    
    print("The value 'n' you input is too large so we take is as infinity")

    result = a/(1-r)
    print(f"The GP = {result}")

gp_r_less_than_1()
gp_r_greater_than_1()
gp_n_is_inf()