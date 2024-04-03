#Task 1
def squares(a, b):
    for n in range(a, b + 1):
        yield n ** 2
        
#Task 2
def even_numbers(n):
    return ', '.join(str(i) for i in range(0, n + 1) if i % 2 == 0)

n = int(input("Enter a number: "))
print("Even numbers between 0 and", n, "in comma separated form:", even_numbers(n))

#Task 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
#Task 4
def squares(a, b):
    for n in range(a, b + 1):
        yield n ** 2

for square in squares(0, 10):
    print(square)
    
#Task 5
def numbers_down_to_0(n):
    for i in range(n, -1, -1):
        yield i

for number in numbers_down_to_0(10):
    print(number)