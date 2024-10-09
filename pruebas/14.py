# STRINGS ARE ARRAYS 

a = "Hello, World!"
print(a[1]) # Will show 'e'

# LOOPING THROUGH A STRING 

for x in "banana":
    print(x) # Will show each letter of the string 'banana'

# STRING LENGTH 

a = "Hello, World!"
print(len(a)) # Will show '13' like the length of the string

# CHECK STRING 
# To check if a certain phrase or character is present in a string, we can use the keyword 'in'

txt = "The best things in life are free like oxigen!"
if "free" in txt:
  print("Yes, 'free' is present.")

# CHECK IF NOT 
txtTwo = "The best things in life are free!"
if "expensive" not in txtTwo:
  print("No, 'expensive' is NOT present.")

# SLICING 
# You can return a range of characters by using the slice syntax.

b = "Hello, World!"
print(b[2:5]) # Will show 'llo'

c = "Hello, World!"
print(c[:5]) # Will show 'Hello'

d = "Hello, World!"
print(d[2:]) # Will show 'llo, World'

f = "Hello, World!"
print(f[-5:-2]) # Will show 'orl'  
# Negative indexing starts the count from the end of the string.