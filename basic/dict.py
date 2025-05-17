band = {
  "vocals": "Plant",
  "guitar": "Page"
}

band2 = dict(vocals ="Plants", guitar="Page", drum = "Disco")

# print(band)
# print(band2)
# print(type(band2))
# print(len(band2))

#access items
print(band["guitar"])
print(band2["drum"])

# list all keys
print(band2.keys())
print(band.values())

# list key/value as tuples
# print(band.items())

# for item in band.items():
#   (key, value) = item
#   print(f"band key {key}'s value is {value}")

# varifies keys
print("guitar" in band2)
print("triangle" in band2)
print("drum" in band2)

# add key
band["drum"] = "Bonham"
print("band updated \n", band)

# remove item
print(band2.pop('guitar'))
print("band2 updated \n", band2)

#remove last item
print(band.popitem())
print(band)

# delete and clear
print(band2.clear()) # return empty dict
del band2 # remove dict

# create reference

band2 = band # access same dict of band

print('band', band)
print('band2', band2) # bad effect

band3 = band.copy() # shallow copy of dict
band3["bass"] = "Colorado"

copy_band = dict(band) # good copy
copy_band['bass'] = "nwe prue"
print(band)
print(band3)
print(copy_band)


