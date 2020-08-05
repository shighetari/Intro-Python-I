# how do we define a function in Python?
def mult2(n):
    return n*2
num = 50
print(mult2(num))
# define a fuction that receives a list of numbers and multiplies every number in the list by 2
# should this function affect the input list?
# or should it return a new list with the multiplied values?
def mul2_list(l):
    # affect the input list
    # iterate over every list element
    for i in range(len(l)):
        # update it to be equal to the current value * 2
        l[i] *= 2  # same as l[i] = l[i] * 2
nums = [10, 60, 4, 15]
mul2_list(nums)
print(nums)
def mult2_new_list(l):
    # creates a new list with the updated values
    new_list = []
    for i in range(len(l)):
        new_list.append(l[i] * 2)
    # we need to return `new_list` here so that it can make its way outside this function
    return new_list
print(mult2_new_list([3, 5, 34, 10, 15]))