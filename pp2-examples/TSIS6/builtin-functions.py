#Task 1
def multiply_numbers(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

numbers = [2, 3, 4, 5]
result = multiply_numbers(numbers)
print("Product of numbers:", result)

#Task 2
def count_letters(string):
    upper_case_count = len(string) - string.count('_') - string.count(' ') - string.count('0') - string.count('1') - string.count('2') - string.count('3') - string.count('4') - string.count('5') - string.count('6') - string.count('7') - string.count('8') - string.count('9')
    lower_case_count = len(string) - upper_case_count
    return upper_case_count, lower_case_count

string = 'Hello World_test_123'
upper_case_count, lower_case_count = count_letters(string)
print("Upper case letters:", upper_case_count)
print("Lower case letters:", lower_case_count)

#Task 3
def is_palindrome(string):
    return string == ''.join(reversed(string))

string = 'racecar'
print("Is palindrome:", is_palindrome(string))

#Task 4
import time
import math

def square_root(number):
    return math.sqrt(number)

milliseconds = 2123
time.sleep(milliseconds / 1000)
result = square_root(25100)
print("Square root of 25100 after 2123 miliseconds is", result)

#Task 5
def all_true(tuple):
    return all(tuple)

tuple = (True, True, True)
tuplen = (True, False, True)
print("All elements are true:", all_true(tuple))
print("All elements are not true:", all_true(tuplen))