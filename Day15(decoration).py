# it takes fuction as arguments and returns a function

def deco(func):
    def new_func(val1, val2):
        if type(val1) == type(val2):
            return func(val1,val2)
        else:
            return func(str(val1),str(val2))
    return new_func

@deco
def concat(val1, val2):
    return val1 + val2
result = concat(10,10)
print(result)


result = concat('hello','world')
print(result)

result = concat('rint',10)
print(result)



