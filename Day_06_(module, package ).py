import re
import test_module


result = test_module.reverse_string('Mike')
print(result)


# ## For a package 
# __init__

# Regular expression

# you need to import re


#  . aline with any character
#  [] to specify range [a - z] , [A - Z], [0 - 9]
# [a-zA-Z] matches a or b or c ... or z A ...B.. or Z
#  + atleast one character [a - z]+ at least one chracter in a to z
#  * zero or more characters [A - Z]*
#  ^ match at the start of a string 
#  $ match at the end of a string
#  ? use to specify optional
#  {} specify nummber of ocurances [a-z]{4} expect 4 occurances of  character
  #  [a - z]{2,4} expect atleast 2 occurances or atmost 4
# \s for sapce
# ()
# \d = [0-9]
# \D = [^0-9] (Not digit)
# \w = [a-zA-z0-9] (Alphanumeric)
# \W = Not alphanumeric
# \s space
# \S not sapce


  #  ## examples 

s = "ABCDE1234A"
# specify the reg
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l)

# s = "8123456789"
# r2 = re.compile("^[1-9][0-9]{9}$")
# print(re.findall(r2,s))


s = "+91 8123456789"
r2 = re.compile("(\+91\s)?[1-9][0-9]{9}$")
result = re.search(r2,s)


if result:
    print(result.group())
else:
    print('not found')
