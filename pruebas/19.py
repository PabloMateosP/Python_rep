# BOOLEANS 

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is bigger than a")
else:
  print("b is not bigger than a")

# EVALUATE VALUES AND VARIABLES 

# Evaluate a string aand a number 
print(bool("Hello"))
print(bool(15))

# Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y)) 

""" 
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones. 
"""

# SOME VALUES ARE FALSE

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# FUNCTIONS CAN RETURN BOOLEAN 
def myFunction() :
  return True

print(myFunction())