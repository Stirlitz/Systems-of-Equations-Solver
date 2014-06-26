# Peter Fajner
# 2014-06-26

# Linear equation solver, two variables in standard form.

import sys

def LinearEquationsTwoVariables():

    eqs = [[] for i in range(2)] # holds the coefficient values for both equations

    for i in range(2):

        eq = (raw_input("Enter equation #" + str(i+1) + ": ").lower())

        a, r = eq.split("x") # finds x coefficient
        b, r = r.split("y") # finds y coefficient

        exit = 0 # apparently I can't raise SystemExit from within a try block (which makes sense), so this is a workaround

        try:
            c, r = r.split("=") # attempts isolate c coefficient from equal sign, if present
            if int(r) != 0: # if whatever is to the right of equal sign is not zero, equation is not in standard form; exits program
                print "Equation " + str(i+1) + " not in standard form!"
                exit = 1
        except:
            c = r

        if exit == 1: raise SystemExit

        try:
            a = float(a) # convert a to a double
        except:
            a = 1.0 # if a is not a number (i.e. isn't present; a cannot be negative), make it 1
        try:
            b = float(b) # convert b to a double
        except:
            if b == '-': b = -1.0 # if b is not a number but is a '-', make it -1
            else: b = 1.0 # if b is not present, make it 1
        try:
            c = float(c) # convert c to a double
        except:
            c = 0.0 # if c is not a number, it isn't present, therefore it is 0

        eqs[i].append(a) # add the variables to the main list
        eqs[i].append(b)
        eqs[i].append(c)

    if eqs[0][0] / eqs[1][0] == eqs[0][1] / eqs[1][1] == eqs[0][2] / eqs[1][2]: # check for equal lines
        return "Lines are the same; infinite number of solutions."

    elif eqs[0][0] / eqs[1][0] == eqs[0][1] / eqs[1][1]: # check for parallel lines
        return "Lines are parallel; no solution."

    y = (eqs[0][0]*eqs[1][2] - eqs[1][0]*eqs[0][2]) / (eqs[1][0]*eqs[0][1] - eqs[0][0]*eqs[1][1]) # determine y
    x = -1*(eqs[0][1]*y + eqs[0][2])/eqs[0][0] # determine x

    solution = [x,y]
    return solution

print "\nEquations must be linear, in standard form (equal to zero), and both variables must be non-zero! Example: 3x+4y-2=0"

print LinearEquationsTwoVariables(), "\n"

raw_input("Press any key to exit... ")