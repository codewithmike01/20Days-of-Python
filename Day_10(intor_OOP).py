
# defining a class
class Account:
    def __init__(self, cust_id, name, initial_bal= 0):
          # To make a private varible
          # use double underscore
          # self.__variableName
          # Then you will need a getter and setter method
          # To access it outside the class
          self.id = cust_id
          self.name = name
          self.balance = initial_bal

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if (amount > self.balance):
            return 'You balance is lesser'
        else:
            self.balance -= amount
            return 'deposited sucessfully'

# crating object for the class

customer1 = Account(1, 'John')
customer2 = Account(2, 'Frank')
customer3 = Account(3, 'Samson')

print(customer1.id)

customer1.deposit(300)
print(customer1.get_balance())
result = customer1.withdraw(50)
print(result)
print(customer1.get_balance())
