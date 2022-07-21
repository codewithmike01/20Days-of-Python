# Strings are Immutable at thesame memory location
# String is a an ordered data structure
# It support indexing and slicing

s = 'Python newbie'

# Indexing
print(s[2])
# Prints t

# Slicing
print(s[0:3]) 
# Prints Pyt

# Stride
# Print every charater of the specified value
print(s[::2])
# print 

# PLace holder formating
num = 12
num2 = 14

print('Value of num1 id {} value of num2 is {}'.format(num, num2))

# Also
print('Value of num1 id {val1} value of num2 is {val2}'.format(val1 = 50, val2 = 40))

print('upper',s.upper())
# All element are turned to uppercase
print('lower',s.lower())
print('capitalize',s.capitalize())
# JUst the first letter in the first letter of the word uppercase 
print('title', s.title())
# More like camel cases

# ## Slipt and join
s1 = 'Html, css, javascript'
print(s1.split(','))

s2 = ['Html', ' css', ' javascript']
print((' ').join(s2))