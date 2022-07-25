# Fuction helps in code reuse
# modularity

def sum_num(a,b = 10):
    return a + b 


print(sum_num(4))

# Aggregate arguments

def sum_all(*args):
        sum = 0
        for value in args:
                sum += value
        return sum

result = sum_all(200,20,100,150,500)
print(result)