# Modes of file open
# r read mode
# r+
# w  write
# w+
# a  append
# a+

# open('file_name', 'mode')

file = open('text_a.txt','r')
content = file.read()

# To specify the 
# number of characters needed to be read
# file.read(20) thats 20 character;
print(content)

# for x in content:
#     print(x)
# file.close()

# Using read gets the text as string
# Using readline() prints each line separated by a newline character \n


#  #### Opening file as Write

file = open('text_write','w')
file.write('I am the writing boy')