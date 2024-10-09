# GLOBAL VARIABLES 
# ================
# Variables that are created outside of a function 

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunctwo():
    x = "fantastic"
    print("Python is " + x)

myfunctwo() # The value of 'x' will be 'fantastic' 

# GLOBAL KEYWORD 
# ============== 
# When you create a variable inside a function, 
# that variable is local, and can only be used inside that function.

def myfuncthree():
  global x
  x = "fantastic"
  print("Python is " + x)

myfuncthree() # x will be 'fantastic'

print("Python is " + x) # x will be 'fantastic' not 'awesome'