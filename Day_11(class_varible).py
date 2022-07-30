# Class variable
# class method starts with @classmethod
# Static method  starts with @staticmethod has no extra parameters


class Account:
    # Class variable
    # It accessed by all object
    # want to cout nuber of customers
    # Can be access with the class name and its variable and also with the object
    # Account.count
    # Only use class name to access and modify the class variable
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


print(Account.get_count())
Account.print_val()