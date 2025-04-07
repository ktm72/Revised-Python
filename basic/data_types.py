x = 10
y = 'Name'

# print(type(x), '\n.....')
# print(type(y),'\n.....')
# print(type(y) == str,'\n.....')
# print(isinstance(y, str),'\n.....')

# constructor function
# pizza = str('Pizza')
# print(type(pizza),'\n.....')
# print(type(pizza) == str,'\n.....')
# print(isinstance(pizza, str),'\n.....')

# concatenation
first = 'Tanvir'
last = 'Mahmud'

fullname = first + " " + last
# print(fullname, '\n.....')

# casting a number to a string

decade = str(1980)
print(type(decade), '\n.....')
statement = "I love rock music from the " + decade +"s."
print(statement)

# multi lines
multiline = '''
       Hey, how are you?
I'm doing great.
All good?       
'''

print(multiline.strip())
print(multiline.rstrip())
print(multiline.lstrip())