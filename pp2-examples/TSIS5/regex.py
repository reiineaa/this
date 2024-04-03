#Task 1
import re

pattern = r'a(b*)'
string = 'abbb'
match = re.match(pattern, string)

if match:
    print("Match found:", match.group(1))
else:
    print("No match found")
    
#Task 2
import re

pattern = r'a(b{2,3})'
string = 'abbb'
match = re.match(pattern, string)

if match:
    print("Match found:", match.group(1))
else:
    print("No match found")
    
#Task 3
import re

pattern = r'[a-z]+(_[a-z]+)*'
string = 'hello_world_test_123'
matches = re.findall(pattern, string)

for match in matches:
    print("Match found:", match)
    
#Task 4
import re

pattern = r'[A-Z][a-z]+'
string = 'Hello World_test_123'
matches = re.findall(pattern, string)

for match in matches:
    print("Match found:", match)
    
#Task 5
import re

pattern = r'a.*b$'
string = 'abbb'
match = re.match(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
    
#Task 6
import re

pattern = r'[ ,.]'
string = 'Hello, World. Test 123'
replaced_string = re.sub(pattern, ':', string)
print("Replaced string:", replaced_string)

#Task 7
import re

def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0]
    for word in words[1:]:
        camel_case_string += word.capitalize()
    return camel_case_string

snake_case_string = 'hello_world_test_123'
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case string:", camel_case_string)

#Task 8
import re

pattern = r'(?<=[a-z])(?=[A-Z])'
string = 'Hello World_test_123'
split_string = re.split(pattern, string)
print("Split string:", split_string)

#Task 9
import re

pattern = r'(?<=[a-z])(?=[A-Z])'
string = 'Hello World_test_123'
inserted_string = re.sub(pattern, ' ', string)
print("Inserted string:", inserted_string)

#Task 10
import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', camel_case_string).lower()
    return snake_case_string

camel_case_string = 'Hello World_test_123'
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case string:", snake_case_string)