 # List, Dict and Set Comprehension
# Map. filter, and lambda

# List comprehension is usful in
# performing task quickly
# Code without list comprehemsion
l = [2,3,4,5,6,7]
l2 = []
for value in l:
    l2.append(value * value)

print(l2)

# Code with list comprehension
lc = [2,3,4,5,6,7]
# [output loop condition]
lc2 = [value * value for value in lc]
print(lc2)

# Finding even numbers in a list
# Using loop comprehension
lce = [23,7,12,90,6,10]
lce2 = [value for value in lce if value % 2 == 0]
print(lce2)

# Finfing the length of strings in an array
lca = ['hello','bobby','sammy','hopvelyn']
lca2 = [len(value) for value in lca]
print(lca2)

# For multiple output
lmo = [200,5,10,12,34]
lmo2 = ['Even' if value % 2 == 0 else 'Odd'  for value in lmo]
print(lmo2)

# ## Comprehension on Dist

d={ x:x**2 for x in range(0,8)}
print(d)



# Comprehention in Set
s= { value**2 for value in range(2,5)}

print(s, type(s))
