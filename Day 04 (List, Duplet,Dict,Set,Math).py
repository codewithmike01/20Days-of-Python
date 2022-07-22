# List in python
l= [3,6,2,6]

# Checking type
print(type(l))
# List

# Operations Add Delete Indexing Slicing
# It can store anytype of data


# Indexing and slicing
print(l[3])
print(l[::2])

# Adding to list
l.append('mike')
print(l)
# Adding multiple element use Extend
# It append each elements one after the other 
l.extend([3,90])
print(l)


# Ading element in between use Instert
# l.insert(index, element_to_add)
l.insert(2, 'In index 2')
print(l)

# USe copy to copy a list

l2 = l.copy()
l.append('last born')
print(l, l2)
