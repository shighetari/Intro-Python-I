# In Python, arrays are called "lists"
# create an empty list
empty = []
# create a list with some numbers
nums = [10, 60, 20, 5]
# print out our list of numbers
# print(nums)
# add a number to our `nums` list
nums.append(77)
# print(nums)
# let's print out every value in the `nums` list one at a time
# for elem in nums:
#     print(elem)
# for (let i=0, i <nums.length, i++)
# what if we want to iterate x number of times?
# for n in range(10):
#     print(n)
# for n in range(2,10):
#     print(n)
# what if we want to iterate along the length of a list? 
for i in range(len(nums)):
    print(i, nums[i])
# another way to print out elements from a list with their assiociated index
for index, value in enumerate(nums):
    print(index, value)

    import sys
import calendar
from datetime import datetime

current_month = datetime.now().month
current_year = datetime.now().year

# if no input print the calendar for the current month
if len(sys.argv) == 1:
  # print(calendar.month(current_year, current_month))
  calendar.prmonth(current_year, current_month)
# if passing one arg, assume month is being passed and render the calendar for the passed month of the current year
elif len(sys.argv) == 2:
   # print(calendar.month(args[2], current_year))
  calendar.prmonth(current_year, int(sys.argv[1]))
# if passing two args, render the calendar for the year and the month
elif len(sys.argv) == 3:
    # print(calendar.month(args[2], args[3]))
  calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
  print('Usage: 14_cal.py [month] [year]')