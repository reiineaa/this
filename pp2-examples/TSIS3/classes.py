#Task 1
class String:
    def __init__(self):
        self.input = ""

    def getString(self):
        self.input = input()

    def upString(self):
        print(self.input.upper())

str = String()
str.getString()
str.upString()
        
#Task2
class Shape:
    def __init__(self, area=0):
        self.area = area

class Square(Shape):
    shape_name = "Square"

    def __init__(self, length):
        self.length = length
        self.area = self.length ** 2

#Task3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(0)  # initialize area to 0
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        return self.area
    
#Task 4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
#Task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount")
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount")
            return False

# Instantiate the Account class
my_account = Account("John Doe", 1000)

# Make several deposits and withdrawals
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500)

# Check the account balance
print("Account owner:", my_account.owner)
print("Account balance:", my_account.balance)

#Task 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

prime_numbers = filter(lambda x: is_prime(x), numbers)

print(list(prime_numbers))