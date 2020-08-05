"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
#print("The script has the name %s" % (sys.argv[0]))

for i in range(len(sys.argv)):
    print('Arguments in sys.argv:** ', sys.argv[i], '**')

# Print out the OS platform you're using:

print("OS platform: ** %s**" % (sys.platform))

# Print out the version of Python you're using:

print("the version of Python you're using is : ** %s**" % (sys.version))


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# print("process ID: %s " % (os.ctermid()))
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
print(os.getlogin())
