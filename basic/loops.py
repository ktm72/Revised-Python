# value = 0
# while value <= 10:
#   print(value)
#   if value == 5:
#     break # break loop at a condition
#   value += 1

# print("<<<<< new loop >>>>")
# print("current value", value)
# while value <= 10:
#   value += 1
#   if value == 6:
#     continue # skip the current loop action at a condition
#   print(value)

names = ["dave", "tanvir", "hasib", "rafi"]

# for x in names:
#   print(x)
for index, value in enumerate(names):
  print(index, value)

# for x in "Mississippi":
#   print(x)

# for x in range(5): #except 5
#   print(x)
for x in range(2, 5): #except 5
  print(x)
for x in range(2, 11, 2): # start, before end, increment
  print(x)
else:
  print("Glad that\'s over!")
