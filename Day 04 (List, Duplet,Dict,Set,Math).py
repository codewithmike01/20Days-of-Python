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

# Pop remove from the last and also by index if argument passed
# Remove : remove element by value
# Clear : to delete all element in the list, return empty list
# del : delete the list 

# sort a list. sorts the original list

l3 = [30,20.70,12,3,5]
l3.sort()
# or l4 = sorted(l3)
print(l3)

# reverse a list
print(l3[::-1])



#  ## Tuple
#  alone have splicing , index and count
t = (9,3,5, 'hello')
print(t)
# index 
print(t[2])

# converting tuble to list
lis = list(t)
print(lis)

# ## Dict It has a key and a value
# Dictionary are mutable, 


d = {'name': 'Mike'}
d['age'] = 43

print(d['name'])
print(d)