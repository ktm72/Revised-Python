squred = lambda num : num * num
print(squred(5))
# Output: 25

addtwo = lambda x, y: x + y
print(addtwo(3, 4))
# Output: 7

def funcBuilder(x):
    return lambda y: x + y
addWithFive = funcBuilder(5)
addWithTen = funcBuilder(10)
addWithTwenty = funcBuilder(20)
print(addWithFive(10))
print(addWithTen(10))
print(addWithTwenty(10))


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)


odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

from functools import reduce
sum_of_numbers = reduce(lambda acc, curr: acc + curr, numbers, 0)
print(sum_of_numbers)
