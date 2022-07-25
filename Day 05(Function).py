# Fuction helps in code reuse
# modularity

def sum_num(a,b = 10):
    return a + b 


print(sum_num(4))

# Aggregate arguments
# arge as in Tuple datatype

def sum_all(*args):
        sum = 0
        for value in args:
                sum += value
        return sum

result = sum_all(200,20,100,150,500)
print(result)

# Keyword aarguments
# Are in dictionary data type

def employee_info(**empy):
    print('{} is {} years old and earns a monthly salary of {}'.format(empy['name'], empy['age'],empy['salary'])) 

employee_info(name = 'Mike', age = 23, salary = '$45000')