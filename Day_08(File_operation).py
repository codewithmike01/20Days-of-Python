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
print(content)

