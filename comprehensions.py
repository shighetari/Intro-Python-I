# say we want to store all of the even numbers in the range
# 0 -100 in a list
# what are some ways we can do this?

# evens_1 = []

# loop through the range
# for i in range(101):
# check if the current number is even
# if i % 2 == 0:
# if it is, add it to the `evens` list
# evens_1.append(i)

# print(evens)


# comprehensions allow us to write the above logic in a much more terse fashion
# evens_2 = [i for i in range(101) if i % 2 == 0]
# print(evens_1 == evens_2)


# create a list of the square values of numbers in the range 1-100

squares_1 = []
for i in range(1, 11):
    squares_1.append(i**2)
    # print(squares_1)
# now we are comparing if the two are the same
squares_2 = [i**2 for i in range(1, 11)]
print(squares_1 == squares_2)


# Create a new list containing only the names that start with `s`
# and also make sure all of the names are properly captialized
# names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

# s_names = []
# for name in names:
#     # check if the names starts with `s`
#     # if it does, add it to `s_names`, making sure the name if properly capitalized
#     if name[0].lower() == "s":
#         s_names.append(name.capitalize())
# print(s_names)

names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

s_names = [name.capitalize()


           for name in names if name[0].lower() == "s"]
print(s_names)

# comprehensions work just as well with dictionaries as well
# populate a dictionary with all letters of the alphabet with their corresponding place in the alphabet
letters = "abcdefghijklmnopqrstuvwxyz"
# alpha = {}

alpha = {letter: i + 1 for i, letter in enumerate(letters)}
#     alpha[letter] = i+1
print(alpha)
