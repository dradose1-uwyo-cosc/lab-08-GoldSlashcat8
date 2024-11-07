# Chauncy Hendon
# UWYO COSC 1010
# Submission Date: 11/7/2024
# Lab 8
# Lab Section: 12
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

print()

def checkIntFloat(inputString):
    """Checks if a string is an int or a float"""
    numdecimals = 0
    numminus = 0
    for item in inputString:
        if item.isdigit():
            pass
        elif item == ".":
            numdecimals += 1
        elif item == "-":
            numminus += 1
        elif item.isdigit() == False:
            return False
    
    if numdecimals == 1:
        return float(inputString)
    elif numdecimals > 1:
        return False
    elif numminus > 1:
        return False
    elif numdecimals == 0:
        return int(inputString)

print(f"Check 1: {type(checkIntFloat("0"))}")
print(checkIntFloat("0"))


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, xlow, xhigh):
    """y = mx + b"""

    range_of_x = []
    values_of_y = []

    if int(xlow) < int(xhigh):
        for item in range(int(xlow), int(xhigh)+1):
            range_of_x.append(item)
    else:
        return("Invalid range for x, inset intergers only")

    while range_of_x:
        x_val = range_of_x.pop()
        print(f"X-val: {x_val}")
        values_of_y.append(float(m)*float(x_val) + float(b))    
    
    return values_of_y
            
while True:
    slope = input("Please give a value for m (e for exit): ")
    if slope == "e":
        break
    intercept = input("Please give a value for b: ")
    if intercept == "e":
        break
    xlower = input("Pleae give a value for lower bound of x: ")
    if xlower == "e":
        break
    xupper = input("Please give an input for the upper bound of x: ")
    if xupper == "e":
        break
    
    print(type(checkIntFloat(slope)))
    print(checkIntFloat(slope))

    if checkIntFloat(slope) == False or checkIntFloat(intercept) == False or checkIntFloat(xlower) == False or checkIntFloat(xupper) == False:
        if checkIntFloat(slope) == 0 or checkIntFloat(intercept) == 0 or checkIntFloat(xlower) == 0 or checkIntFloat(xupper) == 0:
            print(slope_intercept(slope,intercept,xlower,xupper))
        else:
            print("Not accepted, try again")
    else:
        print(slope_intercept(slope,intercept,xlower,xupper))

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadFormula(a, b, c):
    """Solves the quadratic formula"""
    #-b += (b^2 - 4ac)^1/2 / 2a

    insideRoot = float(b)**2 - 4*float(a)*float(c)
    denominator = 2*float(a)
    outside_b = -1 * float(b)

    if insideRoot < 0:
        i = True
    
    
    numerator_positive = outside_b + insideRoot**0.5
    print(numerator_positive)
    numerator_negative = outside_b - insideRoot**0.5
    print(numerator_negative)

    if denominator == 0:
        return "0 failure"

    positive_answer = numerator_positive / denominator
    negative_answer = numerator_negative / denominator

    return positive_answer, negative_answer

while True:
    a_val = input("Please input a val (e to exit): ")
    if a_val == "e":
        break
    b_val = input("Please input b val (e to exit): ")
    if a_val == "e":
        break
    c_val = input("Please input c val (e to exit): ")
    if a_val == "e":
        break

    if checkIntFloat(a_val) == False or checkIntFloat(b_val) == False or checkIntFloat(c_val) == False:
        if checkIntFloat(a_val) == 0 or checkIntFloat(b_val) == 0 or checkIntFloat(c_val) == 0:
            print(quadFormula(a_val,b_val,c_val))
        else:
            print("Not accepted, try again")
    else:
        print(quadFormula(a_val,b_val,c_val))
