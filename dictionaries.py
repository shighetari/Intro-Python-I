# JS objects
# Swift Dictionaries
# Java Hashmaps

# init an empty dictionary

d = {}

# create a dictionary with
# One primary use-case is to associate keys with values
# Dictionaries provide very effecient fetching of keys
# Dictionaries provide de-duplication functionality since they
# never store duplicates of any keys

# create a dictionary with 2 key-value pairs
e = {"foo": 12, 11: "bar"}

print(e["foo"])
print(e[11])

# iterate through dictionary key pairs

for key in e:
    print(key, e[key])

# iterate through key-value pairs
for key, val in e.items():
    print(key, val)

# the `items` method on dictionary is similar to the `enumerate`  function for lists in that both
# give you acess to index-value / key-value
