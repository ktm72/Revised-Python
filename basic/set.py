nums = { 1, 2, 3, 4 }

nums2 = set((1, 2, 3, 3, 4, 5))


# print(nums)
# print(type(nums))
# print(len(nums))

# print(nums2)
# print(type(nums2))
# print(len(nums2))

nums3 = { 1, 2, True, 3, 4, False, 0} # True = 1, False = 0
print(nums3) # ordered and removed duplicate

# check if a value in a set

print( 2 in nums3)

# add a value
# nums.add(9)
# nums.remove(2)
# print(nums)

# more_nums = { 6, 7, 8 }
# nums.update(more_nums)
# print(nums)

# merge two sets 
randoms = { 1, 2 ,3 }
randoms2 = { 7, 8, 9 }

newset = randoms.union(randoms2) # immutable
print(randoms)
print(newset)

# keep duplicates

one = { 1, 2, 3 }
two = { 2, 3, 4 }
one.intersection_update(two) # mutable
print(one)

one = { 1, 2, 3 }
two = { 2, 3, 4 }

# except duplicates
one.symmetric_difference_update(two) # mutable
print(one)