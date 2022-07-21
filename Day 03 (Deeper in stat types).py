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