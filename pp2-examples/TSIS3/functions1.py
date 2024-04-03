#Task 1
def convert_grams_to_ounces():
    grams = float(input("Enter the weight in grams: "))
    ounces = grams * 28.3495231
    print(f"{grams} grams is equal to {ounces} ounces.")

convert_grams_to_ounces()

#Task 2
def fahrenheit_to_centigrade(fahrenheit):
    """Convert Fahrenheit temperature to centigrade."""
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Enter the Fahrenheit temperature: "))
centigrade = fahrenheit_to_centigrade(fahrenheit)

print(f"{fahrenheit} degrees Fahrenheit is equal to {centigrade:.2f} degrees Centigrade.")

#Task 3
def solve(numheads, numlegs):
    if (numlegs > numheads) and (numlegs % 2 == 0):
        rabbit = (numlegs - 2 * numheads) // 2
        chick = numheads - rabbit
        print(f' There are {rabbit} Rabbits and {chick} chickens.')

# Call the function with the given number of heads and legs
solve(35, 94)

#Task 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

#Task 5
def permute(string):
    if len(string) == 0:
        print('')
    else:
        for i in range(len(string)):
            ch = string[i]
            rest_string = string[0:i] + string[i+1:len(string)]
            permute(rest_string)
            print(ch, end='')
        print('')

# Call the function
permute('abc')

#Task 6
def reverse_sentence(string):
    words = string.split()
    return ' '.join(reversed(words))

# Call the function
print(reverse_sentence('We are ready'))

#Task 7
def spy_game(nums):
    return '007' in ''.join(map(str, nums))

# Call the function
print(spy_game([1,2,4,0,0,7,5]))

#Task 8
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Call the function
print(has_33([1,3,3]))

#Task 9
import math

def sphere_volume(radius):
    return 4/3 * math.pi * (radius**3)

# Call the function
print(sphere_volume(5))

#Task 10
def unique_list(nums):
    return [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i-1]]

# Call the function
print(unique_list([1,1,2,2,3,4,5,5]))

#Task 11
def is_palindrome(string):
    return string == string[::-1]

# Call the function
print(is_palindrome('racecar'))

#Task 12
def histogram(nums):
    for i in nums:
        print('*' * i)

# Call the function
histogram([4, 9, 7])

#Task 13
import random

def guess_game():
    number = random.randint(1, 20)
    guess = -1
    count = 0

    while guess != number:
        guess = int(input('Take a guess: '))
        count += 1
        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')

    print(f'Good job, {name}! You guessed my number in {count} guesses!')

# Call the function
name = input('Hello! What is your name? ')
guess_game()