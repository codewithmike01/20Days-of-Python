# INheritance
# Multiple inheritance

class Account:
    count = 0
    # Class methods
    @classmethod
    def incr_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod 
    def print_val():
        print('This is a static method oh yea')

    def __init__(self, cust_id, name, initial_bal= 0):
        # Instace variable
          Account.incr_count()
          self.__id = cust_id
          self.__name = name
          self.__balance = initial_bal

    def get_balance(self):
        return self.__balance
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if (amount > self.__balance):
            return 'You balance is lesser'
        else:
            self.__balance -= amount
            return 'deposited sucessfully'

# crating object for the class

customer1 = Account(1, 'John')
customer2 = Account(2, 'Frank')
customer3 = Account(3, 'Samson')

# Inheritance class
# it would have a parenthesis 
# and have an argument of 
# the class it is inheriting from
# in this case we are inheriting from 
# Account class


class Savings(Account):
    
    def __init__(self, cust_id, name, initial_bal = 0):
        super().__init__(cust_id , name, initial_bal )
        self.limit = 5000
      
    def withdraw(self, amount):
        if amount < self.limit:
            bal_result = super().withdraw(amount)
            self.limit -= amount
            return bal_result
        else:
            return 'You can not withdraw above the limit set'


cust1 = Savings(5, 'Ovie')
print(cust1)
cust1.deposit(1000)
result = cust1.get_balance()
print(result)

result = cust1.withdraw(3000)
print(result)


# Multiple inheritance

# if class A and B 
# And i want C to inherit form A and B

class A_a:
    pass

class B_b:
    pass

# Inheritance
class C (A_a, B_b):
    pass