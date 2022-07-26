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
