# Modes of file open
# r read mode
# r+ read and append a write
# w  write
# w+ write and read
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

# just write use w
file = open('text_write','w+')
file.write('I am the writing boy')

# Changing pointer position
# tell to tell you where the pointer is located
# seek to change the cyrretn pointer position

# file.tell()
# seek has
  #  offset -- number of charaters
  #  position
    # 0 is start
    # 1 current position of pointer
    # 2 end
# seek(0,0) thats 0 chaacters and cursor to the start
file.seek(0,0)
content = file.read()
print(content)
file.close()

# a a+ cursor position is defaultly at the end 
# a+ can read and write 