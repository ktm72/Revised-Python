users = ["Dave", "Maria", "Abul", "Shin"]

data = ["Dave", 43, True]

emptyList = []

# print("Dave" in users)
# print("Dave" in data)
# print("Dave" in emptyList)


# print(users[0])
# print(users[-1])

# print(users.index("Abul"))
# print(users[0: 2]) # 0 to 1, before index 2
# print(users[-2: -1])
# print(users[1:])

users.append('Pajeet')
print(users[1:])

# users.extend(['Chakz', "Gurung"]) # extend list
# print(users)

# users.insert(1, "Karin") # insert at index 1
# print(users)

# users[2:2] = ["Nasir", "Ashraf"] # insert at index 2 without any replacement
# print(users)

# users[1:3] = ["Nasir", "Ashraf"] # replace from 1 to 2
# print(users)

# users.remove("Ashraf") # remove first occurance of Ashraf
# print(users)

# remove index 1
print(users.pop(1)) # pop return the removed value
print(users)

del users[1] # delete index 1
print(users)

data.clear() # clear the list
print(data)

users.sort() # sort the list
print(users)

users.sort(reverse=True) # sort the list in reverse
users.sort(key=str.lower) # alphabetical order
print(users)


nums = [3,5, 7, 9, 19, 22, 25, 56]
# nums.reverse() # reverse the list
# print(nums)

print(sorted(nums, reverse=True)) # return sorted list without changing the original list
print(nums)

nums2 = nums.copy() # copy the list
nums3 = list(nums) # copy the list
nums4 = nums[:] # copy the list

print(nums2)
print(nums3)
print(nums4)

print(type(nums))
