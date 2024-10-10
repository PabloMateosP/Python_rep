# PYTHON MODIFY STRINGS 

# Upper Case 
a = "Hello, World!"
print(a.upper())

# Lower Case 
b = "Hello, World!"
print(b.lower())

# Remove Whitespace (from the beginning or the end)
# Method lstrip for the left 
# Method rstrip for the right 
c = "   Hello, World!   "
print(c.strip()) # Return "Hello, World!"

# Replace String
d = "Hello, World!"
print(d.replace("H", "J")) # Return "Jello, World!"

# Split String 
e = "Hello, World!"
print(e.split(", ")) # Return ['Hello', 'World!']