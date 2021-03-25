a = "Hello, World welcome to Python String !"

b = "Hello,Python Programmer !"
print(len(a))  # count len String
print(a[2:10])  # Slicing string
print(a.upper())  # Convert all char to upper case
print(a.lower())  # Convert all char to lower cae
print(a.capitalize())  # Capitalize First word first char
print(a.title())  # Capitalize First char of Every Word
print(a.swapcase())
# Swapcase swap all the word (upper to lower and lower to upper)
print(a.casefold())
# Return a version of the string suitable for caseless comparisons.
print(a + ' ' + b)  # to concat two string
c = 42
print(a+' '+'{}'.format(c))
