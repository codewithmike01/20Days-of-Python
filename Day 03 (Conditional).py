# If condition

num = 5
num2 = 2

if num > num2:
    print(num , 'is grater than', num2)
elif num < num2:
    print(num , 'is less than', num2)
else:
    print('Both numbers are equal')
    

# For loop
for s in [3,5,7,12,90,2]:
    print(s * 2)

for value in range(5):
    print(value)

# Use emumerable while working with index
for value,index in enumerate([2,4,6,7,8]):
        print(index, value)



# While loop
n= 2
while n <= 10:
        print('in while loop', n)
        n += 1