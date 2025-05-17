# tuple 
mytuple = tuple(('my', 2, 'rest', 2, True))
print(type(mytuple))

another_tuple = (91, 5 ,9, 3)
print(type(another_tuple))


(one, two, *rest) = another_tuple
print(one)
print(two)
print(rest)

(one, two, *rest) = mytuple
print(f"first entry of mytuple is {one}")
print(f"second entry of mytuple is {two}")
print(f"rest of the entries of mytuple are {rest}")

print(mytuple.count(2)) # count the occurance of 2 in the tuple