a = "hello WORlD!"

# There are 47 methods for strings in Python

# 1) string.capitalize()
# Returns the string where the first character is upper case, and the rest is lower case
print("string.capitalize()")
print(a.capitalize())

# 2) string.casefold()
# Returns the string where all characters are lowercase
# Similar to lower(), but is "stronger" and "more aggressive"
# That is, more characters will be be turned to lowercase
print("string.casefold()")
print(a.casefold())

# 3) string.center(length, character)
# Center aligns the string using a specified character as the fill character
# length - The length of the returned string
# character - The character to fill the missing space. Defaults to " " (Optional)
print("string.center()")
print(a.center(20, "-"))

# 4) string.count(value, start, end)
# Returns the number the specified value appears in the string
# value - The value to search for
# start - The position to start the search; Default value is 0 (Optional)
# end - The position to end the search; Default value is end of the string (Optional)
print("string.count()")
print(a.count("l", 3, 11))

# 5) string.encode(encoding=encoding, errors=errors)
# Encodes the string using the specified encoding
# encoding - The encoding to be used; Default value is UTF-8 (Optional)
# errors - Specify the error method (Optional)
# Legal values for errors include
# 'backslashreplace' - Uses a backslash instead of the character that could not be encoded
# 'ignore' - Ignores the characters that cannot be encoded
# 'namereplace' - Replaces the character with a text explaining the character
# 'strict' - Raises an error on failure (Default value)
# 'replace' - Replaces the character with a question mark
# 'xmlcharrefreplace' - Replaces the character with an XML character
print("string.encode()")
b = "Blåhaj"
print(b.encode(encoding="ascii",errors="backslashreplace"))
print(b.encode(encoding="ascii",errors="ignore"))
print(b.encode(encoding="ascii",errors="namereplace"))
print(b.encode(encoding="ascii",errors="replace"))
print(b.encode(encoding="ascii",errors="xmlcharrefreplace"))

# 6) string.endswith(value, start, end)
# Returns True if string ends with specified value
# value - The value to check if the string ends with; Can also be a tuple, method will return True if it ends with any value in the tuple
# start - The position to start the search; Default value is 0 (Optional)
# end - The position to end the search; Default value is end of the string (Optional)
print("string.endswith()")
c = "0123456"
print(c.endswith("3", 1, 4))
print(c.endswith(("6", "7")))

# 7) string.expandtabs(tabSize)
# Sets the tab size to the specified number of whitespaces
# tabSize - Number specifying the tab size; Default value is 8 (Optional)
print("string.expandtabs()")
d = "H\te\tl\tl\to\tw\to\tr\tl\td"
print(d.expandtabs(4))
print(d.expandtabs())

# 8) string.find(value, start, end)
# Finds the first occurrence of the specified value
# value - The value to search for
# start - The position to start the search; Default value is 0 (Optional)
# end - The position to end the search; Default value is end of the string (Optional)
print("string.find()")
print(a.find("l", 3, 11))

# If the value is not found, it returns -1 which differentiates it from the index() method
print(a.find("q"))

# 9) string.format_map(dictionary)
# Returns the value of the key-value pairs in the dictionary to the string
# dictionary - The dictionary containing key-value pairs
print("string.format_map()")
e = {"age": 22, "name": "Nic"}
f = "My name is {name} and I am {age}"
print(f.format_map(e))

# 10) string.format(value1, value2...)
# Formats the specified value(s) and inserts them within the string's placeholder
# Placeholder can be identified with named indexes, numbered indexes or empty placeholders
# value1, value2... - One or more values that should be formatted and inserted into the string
# These can be either a list of values separated by commas, a key=value list or a combination of both
# Values can be of any data type
print("string.format()")
print(f.format(name="Nic", age=22))
g = "My name is {0} and I am {1}"
print(g.format("Nic", 22))
h = "My name is {} and I am {}"
print(h.format("Nic", 22))

# Formatting types also exist
# :< - Left aligns the result (within the available space)
i = "I am {:<5} years old"
print(i.format(22))

# :> - Right aligns the result (within the available space)
j = "I am {:>5} years old"
print(j.format(22))

# :^ - Center aligns the result (within the available space)
k = "I am {:^5} years old"
print(k.format(22))

# := - Places the sign to the left most position
l = "The lowest temperature in Sapporo today is {:=5}°C"
print(l.format(-3))

# :+ - Use a plus sign to indicate if the result is positive or negative
m = "The temperature in Sapporo today is between {:+}°C and {:+}°C"
print(m.format(-3, 7))

# :- - Use a minus sign for negative values only
n = "The temperature in Sapporo today is between {:-}°C and {:-}°C"
print(n.format(-3, 7))

# :  - Use a space to insert an extra space before positive numbers and a minus sign before negative numbers
o = "The temperature in Sapporo today is between {: }°C and {: }°C"
print(o.format(-3, 7))

# :, - Use a comma as a thousand separator
p = "Tokyo's population as of 2024 is {:,}"
print(p.format(37115000))

# :_ - Use a underscore as a thousand separator
q = "Tokyo's population as of 2024 is {:_}"
print(q.format(37115000))

# :b - Binary format
r = "My age, {0}, in binary is {0:b}"
print(r.format(22))

# :c - Converts the value into the corresponding unicode character
s = 65
print("The encoded codepoint for " + "{:c}".format(s) + " is " + str(s))

# :d - Decimal format
t = 0b10110
print("{:d}".format(t))

# :e - Scientific format, with a lower case e
u = "Tokyo's population in scientific format with a lower case e is {:e}"
print(u.format(37115000))

# :E - Scientific format, with an upper case E
v = "Tokyo's population in scientific format with an upper case E is {:E}"
print(v.format(37115000))

# :f - Convert a number to a fix point number; Defaults to 6 decimals
# The number of decimals can be specified with a full stop (.) followed by a number
w = "The exchange rate between USD and JPY is currently 1 USD = {:f} JPY"
print(w.format(150.60562))
x = "The exchange rate between USD and JPY is currently 1 USD = {:.2f} JPY"
print(x.format(150.60562))
y = "The highest number Python can register is {:f}"
print(y.format(float("inf")))

# :F - Fix point number format, in uppercase format (Show inf and nan as INF and NAN)
z = "0 divided by 0 is {:F}"
print(z.format(float("nan")))

# :g - General format; Which means it
# Removes insignificant trailing 0s
a1 = 0.123456700000000
print("{:g}".format(a1))

# Uses scientific notation for very large or very small numbers
b1 = 0.000000001234567
print("{:g}".format(b1))

# Defaults to six significant digits
c1 = 3.141592653589793
print("Pi to 6 significant figures is " + "{:g}".format(c1))

# Can be specified with a full stop followed by a number
print("Pi to 7 significant figures is " + "{:.7g}".format(c1))

# :G - General format (Using a upper case E for scientific notations)
print("{:G}".format(b1))

# :o - Octal format
d1 = "{0} in decimal is the same as {0:o} in octal"
print(d1.format(9))

# :x - Hex format, lower case
e1 = "{0} in decimal is the same as {0:x} in hexadecimal"
print(e1.format(26))

# :X - Hex format, upper case
f1 = "{0} in decimal is the same as {0:X} in hexadecimal"
print(f1.format(26))

# :n - Number format

# :% - Percentage format
# Defaults to 6 decimal places
g1 = "You scored {:%}"
print(g1.format(0.92))

# Can be specified with a full stop followed by a number
g2 = "You scored {:.0%}"
print(g2.format(0.92))

# 11) string.index(value, start, end)
# Finds the first occurrence of the specified value
# value - The value to search for
# start - Where to start the search; Default value is 0 (Optional)
# end - Where to end the search; Default value is the end of the string (Optional)
print("string.index()")
print(a.index("l", 3, 11))

# Throws an exception if the value is not found, which differs it from the find() method
# print(a.index("q"))

# 12) string.isalnum()
# Returns True if all characters in a string are alphanumeric
# Alphanumeric characters are alphabet letters and numbers
# The method can also be used on Unicode objects
print("string.isalnum()")
h1 = "\u0041\u0030"
print(a.isalnum())
print(h1.isalnum())

# 13) string.isalpha()
# Returns True if all characters in a string are alphabet letters
# The method can also be used on Unicode objects
print("string.isalpha()")
i1 = "\u0041"
print(a.isalpha())
print(i1.isalpha())

# 14) string.isascii()
# Returns True if all characters in a string are ASCII characters
# The method can also be used on Unicode objects
print("string.isascii()")
j1 = "\u0041"
print(a.isascii())
print(j1.isascii())

# 15) string.isdecimal()
# Returns True if all characters in a string are decimals
# The method can also be used on Unicode objects
print("string.isdecimal()")
k1 = "\u0030"
print(a.isdecimal())
print(k1.isdecimal())

# 16) string.isdigit()
# Returns True if all characters in a string are digits
# Exponents, like ², are also considered to be digits
print("string.isdigit()")
l1 = "2²"
print(a.isidentifier())
print(l1.isdigit())

# 17) string.isidentifier()
# Returns True if string is a valid identifier
# Identifiers have the same rules for being valid as a variable
print("string.isidentifier()")
m1 = "valid_Identifi3r"
print(m1.isidentifier())
print(a.isidentifier())

# 18) string.islower()
# Returns True if all alphabet characters in a string are in lower case
# Numbers, symbols and spaces are not checked
print("string.islower()")
print(a.islower())

# 19) string.isnumeric()
# Returns True if all characters in a string are numeric
# Characters like ² or ¾ are considered to be numeric
# Strings like 1.618 or -3.141 are not considered to be numeric
print("string.isnumeric()")
print(a.isnumeric())
print(l1.isnumeric())

# 20) string.isprintable()
# Returns True if all characters in a string can be printed
# Examples of non-printable characters include carriage returns
print("string.isprintable()")
o1 = "New\nLine"
print(a.isprintable())
print(o1.isprintable())

# 21) string.isspace()
# Returns True if all characters in a string are whitespaces
print("string.isspace()")
p1 = "       "
print(a.isspace())
print(p1.isspace())

# 22) string.istitle()
# Returns True if all words in a string start with a capital letter and the rest of the word is in lower case
# Numbers, symbols and spaces are ignored
print("string.istitle()")
q1 = "Hello World"
print(a.istitle())
print(q1.istitle())

# 23) string.isupper()
# Returns True if all characters in a string are capital letters
# Numbers, symbols and spaces are ignored
print("string.isupper()")
r1 = "HELLO WORLD!"
print(a.isupper())
print(r1.isupper())

# 24) string.join(iterable)
# Takes all items in an iterable and joins them into a singular string
# iterable - Any iterable object where the returned values are all strings
print("string.join()")
s1 = ("Apple", "Banana", "Cherry")
print(", ".join(s1))

# 25) string.ljust(length, character)
# Left aligns the given string using a specified character as the fill character
# length - The length of the returned string; This includes the length of the string
# character - The character to fill the missing space; Default value is the space character
print("string.ljust()")
t1 = "Nic"
print(t1.ljust(10, "-") + " is my name")

# 26) string.lower()
# Returns the string where all characters are lower case
# Numbers, symbols and spaces are ignored
print("string.lower()")
print(a.lower())

# 27) string.lstrip(characters)
# Removes any leading characters from the left
# characters - A set of characters to remove as leading characters (Optional); Default value is space
print("string.lstrip()")
u1 = "    ,,,,...ffdddgddgNic    !"
print(u1.lstrip(" ,.fdg"))

# 28) string.maketrans(x, y, z)
# Returns a mapping table that can be used with the translate() method to replace specified characters
# x - If 1 parameter is specified, this has to be a dictionary describing how to perform the replace
# If 2 or more parameters are specified, this parameter has to be a string specifying the characters that are to be replaced
# y - A string with the same length as x
# Each character will be replaced with the corresponding character in this string
# z - A string describing which characters to remove from the original string.
print("string.maketrans()")
w1 = "I'm Luka~"
y1 = "Luka"
z1 = "Nic!"
a2 = "~"
b2 = str.maketrans(y1, z1, a2)
print(w1.translate(b2))

# 29) string.partition(value)
# Searches for a specified string and splits the string into a tuple containing 3 elements
# 1st element - The part before the specified string
# 2nd element - The specified string
# 3rd element - The part after the specified string
# The method only searches for the first occurrence of the specified string
# value - The string to search for
print("string.partition()")
print(a.partition("l"))

# If the specified value is not found, the tuple now returns
# 1st element - The whole string
# 2nd element - An empty string
# 3rd element - An empty string
print(a.partition("q"))

# 30) string.removeprefix(value)
# Removes the specified value at the start of the string and returns the rest of the string
# value - The string to be removed from the start
print("string.removeprefix()")
c2 = "h"
print(a.removeprefix(c2))

# 31) string.removesuffix(value)
# Removes the specified value at the end of the string and returns the rest
# value - The string to be removed from the end
print("string.removesuffix()")
d2 = "!"
print(a.removesuffix(d2))

# 32) string.replace(oldValue, newValue, count)
# Replaces the specified phrase with another specified phrase
# oldValue - The value of the string to search for
# newValue - The string to replace the old value with
# count - Number specifying how many occurrences of the old value you want to replace; Default value is all occurrences
print("string.replace()")
print(a.replace("l", "w", 2))

# 33) string.rfind(value, start, end)
# Finds the last occurrence of the specified value
# value - The value to search for
# start - The position to start the search; Default value is 0 (Optional)
# end - The position to end the search; Default value is end of the string (Optional)
print("string.rfind()")
print(a.rfind("l", 3, 11))

# If the value is not found, it returns -1 which differentiates it from the rindex() method
print(a.rfind("q"))

# 34) string.index(value, start, end)
# Finds the first occurrence of the specified value
# value - The value to search for
# start - Where to start the search; Default value is 0 (Optional)
# end - Where to end the search; Default value is the end of the string (Optional)
print("string.rindex()")
print(a.rindex("l", 3, 11))

# Throws an exception if the value is not found, which differs it from the rfind() method
# print(a.rindex("q"))

# 35) string.rjust(length, character)
# Right aligns the given string using a specified character as the fill character
# length - The length of the returned string; This includes the length of the string
# character - The character to fill the missing space; Default value is the space character
print("string.rjust()")
e2 = "22"
print("My age is " + e2.ljust(10, "-"))

# 36) string.rpartition(value)
# Searches for the last occurrence of a specified string and splits the string into a tuple containing 3 elements
# 1st element - The part before the specified string
# 2nd element - The specified string
# 3rd element - The part after the specified string
# The method only searches for the first occurrence of the specified string
# value - The string to search for
print("string.rpartition()")
print(a.rpartition("l"))

# If the specified value is not found, the tuple now returns
# 1st element - An empty string
# 2nd element - An empty string
# 3rd element - The whole string
print(a.rpartition("q"))

# 37) string.rsplit(separator, maxSplit)
# Splits a string into a list starting from the right
# separator - Specifies the operator when splitting the string; Default value is the whitespace character (Optional)
# maxSplit - Specifies how many splits to do; Default value is -1 which indicates all occurrences - Number of elements in the list is maxSplit + 1 (Optional)
print("string.rsplit()")
f2 = "A, B, C"
print(f2.rsplit(", ", 1))

# 38) string.rstrip(characters)
# Removes any leading characters from the right
# characters - A set of characters to remove as leading characters (Optional); Default value is space
print("string.rstrip()")
g2 = "!    Nic    ,,,,...ffdddgddg"
print(g2.rstrip(" ,.fdg"))

# 39) string.split(separator, maxSplit)
# Splits a string into a list
# separator - Specifies the operator when splitting the string; Default value is the whitespace character (Optional)
# maxSplit - Specifies how many splits to do; Default value is -1 which indicates all occurrences - Number of elements in the list is maxSplit + 1 (Optional)
print("string.split()")
print(f2.split(", ", 1))

# 40) string.splitlines(keepLineBreaks)
# Splits a string at line breaks into a list
# keepLineBreaks - Specifies if the line breaks should be included - Default value is False (Optional)
print("string.splitlines()")
print(o1.splitlines())
print(o1.splitlines(True))

# 41) string.startswith(value, start, end)
# Returns True if string starts with specified value
# value - The value to check if the string starts with; Can also be a tuple, method will return True if it ends with any value in the tuple
# start - The position to start the search; Default value is 0 (Optional)
# end - The position to end the search; Default value is end of the string (Optional)
print("string.endswith()")
c = "0123456"
print(c.startswith("3", 1, 4))
print(c.startswith(("0", "-1")))

# 42) string.strip(characters)
# Removes any leading and trailing whitespaces
# characters - A set of characters to remove as leading characters (Optional); Default value is space
print("string.strip()")
h2 = " ,,,,...ffdddgddgMy name is Nic and I am 22 ,,,,...ffdddgddg"
print(h2.strip(" ,.fdg"))

# 43) string.swapspace()
# Returns the string with lower case as upper case and vice versa
print("string.swapspace()")
print(a.swapcase())

# 44) string.title()
# Returns the string where the first character of every word is upper case
# If the word starts with a number or symbol, the first letter after will be converted to upper case
print("string.title()")
i2 = "1my `name is ~nic"
print(i2.title())

# 45) string.translate(table)
# Returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
# Use the maketrans() method to create a mapping table
# If a character is not specified within the dictionary/table, the character will not be replaced
# If a dictionary is used, ASCII codes must be used instead of characters.
# table - A dictionary or mapping table describing how to perform the replace
print("string.translate()")
print(w1.translate(b2))

# 46) string.upper()
# Returns a string where all characters are in upper case
print("string.upper()")
print(a.upper())

# 47) string.zfill(length)
# Adds 0s at the beginning of the string until the specified length is reached
# If the value of the length parameter is less than the length of the string, no filling is done
# length - A number specifying the desired length of the string
print("string.zfill()")
print(a.zfill(20))