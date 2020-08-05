# how do we print "Hello world" in Python? 
print("Hellow World")
# How does this differ from how you would do it in your core track language?
# JS: console.log('Hellow World')
# How does we ran this program differ from how we'd do it in your core track language?
# iOS: compile the swift file with Xcode, and then run the binary?
# JS: 1. run it in the browser
#   2. node [filename.js]
# Java: 1.compile using the java compiler into a jar file
#   2. execture the jar file
name = "Bob"
# String interpolation using `+`
print("Hello "+ name)
# String interpolation using f-strings
print(f'Hello {name}')
# if statements
# in Python, whitespace is important
if name != "Sean":
    print("Hey, you aren't Sean")
else:
    print(f"Hello {name}")