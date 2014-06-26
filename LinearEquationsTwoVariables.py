# in format ax+by+c=0

eq1 = raw_input("Enter first equation: ").lower()
eq2 = raw_input("Enter second equation: ").lower()

eq1a, eq1r = eq1.split("x")
eq1b, eq1c = eq1r.split("y")

try:
    eq1a = int(eq1a)
except:
    eq1a = 1
try:
    eq1b = int(eq1b)
except:
    if eq1b == '-': eq1b = -1
    else: eq1b = 1
try:
    eq1c = int(eq1c)
except:
    if eq1c == '-': eq1c = -1
    else: eq1c = 1

print eq1a
print eq1b
print eq1c