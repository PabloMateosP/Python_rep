# FORMAT STRINGS 

# f Strings 
age = 36 
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value  
price = 59
txt2 = f"The price is ${price:.2f} dollars" # Display the price with 2 decimals
print(txt2)

# A placeholder can contain Python code, like math operations
txt3 = f"The price is {20 * 59} dollars"
print(txt3)