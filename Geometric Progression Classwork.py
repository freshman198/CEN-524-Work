# OZOKO-EMMANUEL DELIGHT
# 20CJ027488
## COMPUTER ENGINEERING
## CEN 524
#
# Assingment - A python script for the sum of a GP

import math

print("This program calculates the sum of a Geometric Progression (GP) series.")

a = float(input("What is your first number (a)? "))
r = float(input("What is the common ratio (r)? "))
n = int(input("What are the number of terms present? "))

def sum_of_gp(a, r, n):
    if n > 1000000:
        print("The value of 'n' you input is too large so we take is as infinity")
        if abs(r) < 1:   
            result = a/(1-r)
        else:
            return None

    else:
        if abs(r) > 1:
            result = a*(math.pow(r, n)-1)/(r-1)
        elif abs(r) < 1:
            result = a*(1-math.pow(r, n))/(1-r)

    return result

sum_of_gp = sum_of_gp(a, r, n)

if sum_of_gp is not None:
    print(f"The sum of the GP is: {sum_of_gp}")
else:
    raise ValueError("The common ratio must be less than 1 in this equation")

