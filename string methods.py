# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:12:03 2021

@author: TEJA SREE
"""


# 1. capitalize() - Converts the first character to upper case
print("1. capitalize():\n")
text = "i am learning python"
x = text.capitalize()
print(x)




# 2. casefold() - Converts string into lower case
print("\n\n")
print("2. casefold():\n")
text = "I AM LEARNING PYTHON"
x = text.casefold()
print(x)




# 3. center() - Returns a centered string
print("\n\n")
print("3. center():\n")
text = "PYTHON"
x = text.center(15)
print(x)



# 4. count() - Returns the number of times a specified value occurs in a string
print("\n\n")
print("4. count():\n")
text = "I AM LEARNING PYTHON"
x = text.count("A")
print(x)




# 5. encode() - Returns an encoded version of the string
print("\n\n")
print("5. encode():\n")
text = "i am learning python"
x = text.count("A")
print(x)




# 6. endswith() - Returns true if the string ends with the specified value
print("\n\n")
print("6. endswith():\n")
text = "i am learning python"
x = text.endswith("n")
print(x)




# 7. expandtabs() - Sets the tab size of the string
print("\n\n")
print("7. expandtabs():\n")
text = "i\tam\tlearning\tpython"
x = text.expandtabs(4)
print(x)




# 8. find() - Searches the string for a specified value and returns the position of where it was found
print("\n\n")
print("8. find():\n")
text = "i am learning python"
x = text.find("learning")
print(x)




# 9. format() - Formats specified values in a string
print("\n\n")
print("9. format():\n")
text = "I am {name}, I am learning {lang}".format(name = "Teju", lang = "Python")
print(text)



# 10. format_map()	Formats specified values in a string



# 11. index()	Searches the string for a specified value and returns the position of where it was found
print("\n\n")
print("11. index():\n")
text = "i am learning python"
x = text.index("am")
print(x)



# 12. isalnum()	Returns True if all characters in the string are alphanumeric
print("\n\n")
print("12. isalnum():\n")
text = "Python12"
x = text.isalnum()
print(x)



# 13. isalpha()	Returns True if all characters in the string are in the alphabet
print("\n\n")
print("13. isalpha():\n")
text = "Python12"
x = text.isalpha()
print(x)




# 14. isdecimal()	Returns True if all characters in the string are decimals
print("\n\n")
print("14. isdecimal():\n")
text = "\u0030"
x = text.isdecimal()
print(x)



# 15. isdigit()	Returns True if all characters in the string are digits
print("\n\n")
print("15. isdigit():\n")
text = "1512"
x = text.isdigit()
print(x)



# 16. isidentifier()	Returns True if the string is an identifier
print("\n\n")
print("16. isidentifier():\n")
text = "1512"
x = text.isidentifier()
print(x)




# 17. islower()	Returns True if all characters in the string are lower case
print("\n\n")
print("17. islower():\n")
text = "i am learning python"
x = text.islower()
print(x)




# 18. isnumeric()	Returns True if all characters in the string are numeric
print("\n\n")
print("18. isnumeric():\n")
text = "1512"
x = text.isnumeric()
print(x)



# 19. isprintable()	Returns True if all characters in the string are printable
print("\n\n")
print("19. isprintable():\n")
text = "i am learning python"
x = text.isprintable()
print(x)



# 20. isspace()	Returns True if all characters in the string are whitespaces
print("\n\n")
print("20. isspace():\n")
text = "i am learning python"
x = text.isspace()
print(x)




# 21. istitle()	Returns True if the string follows the rules of a title
print("\n\n")
print("21. istitle():\n")
text = "I am learning python"
x = text.istitle()
print(x)



# 22. isupper()	Returns True if all characters in the string are upper case
print("\n\n")
print("22. isupper():\n")
text = "I AM LEARNING PYTHON"
x = text.isupper()
print(x)




# 23. join()	Joins the elements of an iterable to the end of the string
print("\n\n")
print("23. join():\n")
tuple = ("1","2","3")
x = "#".join(tuple)
print(x)




# 24. ljust()	Returns a left justified version of the string
print("\n\n")
print("24. ljust():\n")
txt = "teju"
x = txt.ljust(15, "u")
print(x)



# 25. lower()	Converts a string into lower case
print("\n\n")
print("25. lower():\n")
text = "I AM LEARNING PYTHON"
x = text.lower()
print(x)



# 26. lstrip()	Returns a left trim version of the string
print("\n\n")
print("26. lstrip():\n")
text = "     teju     "
x = text.lstrip()
print("I am ", x, ", studying Python ")





# 27. maketrans()	Returns a translation table to be used in translations
print("\n\n")
print("27. maketrans():\n")
text = "PYTHON"
x = text.maketrans("P", "L")
print(text.translate(x))





# 28. partition()	Returns a tuple where the string is parted into three parts
print("\n\n")
print("28. partition():\n")
text = "I am learning python"
x = text.partition("am")
print(x)



# 29. replace()	Returns a string where a specified value is replaced with a specified value
print("\n\n")
print("29. replace():\n")
text = "I am learning python"
x = text.replace("python", "C++")
print(x)



# 30. rfind()	Searches the string for a specified value and returns the last position of where it was found
print("\n\n")
print("30. rfind():\n")
text = "I am learning python"
x = text.rfind("learning")
print(x)


# 31. rindex()	Searches the string for a specified value and returns the last position of where it was found
print("\n\n")
print("31. rindex():\n")
text = "I am learning python"
x = text.rindex("learning")
print(x)



# 32. rjust()	Returns a right justified version of the string
print("\n\n")
print("32. rjust():\n")
text ="I am"
x = text.rjust(15)
print(x, " learning python")



# 33. rpartition()	Returns a tuple where the string is parted into three parts
print("\n\n")
print("33. rpartition():\n")
text = "I am learning python"
x = text.rpartition("learning")
print(x)




# 34. rsplit()	Splits the string at the specified separator, and returns a list
print("\n\n")
print("34. rsplit():\n")
text = "banana"
x = text.rsplit("a")
print(x)



# 35. rstrip()	Returns a right trim version of the string
print("\n\n")
print("35. rstrip():\n")
text = "     teju     "
x = text.rstrip()
print("I am ", x, ", studying Python ")




# 36. split()	Splits the string at the specified separator, and returns a list
print("\n\n")
print("36. split():\n")
text = "banana"
x = text.split("a")
print(x)



# 37. splitlines()	Splits the string at line breaks and returns a list
print("\n\n")
print("37. splitlines():\n")
text = "I am teju \n I am learning python"
x = text.splitlines()
print(x)


# 38. startswith()	Returns true if the string starts with the specified value
print("\n\n")
print("38. startswith():\n")
text = "I am teju, I am learning python"
x = text.startswith("I")
print(x)



# 39. strip()	Returns a trimmed version of the string
print("\n\n")
print("39. strip():\n")
text = "     teju     "
x = text.strip()
print("I am ", x, ", studying Python ")



# 40. swapcase()	Swaps cases, lower case becomes upper case and vice versa
print("\n\n")
print("40. swapcase():\n")
txt = "teju"
x = txt.swapcase()
print(x)



# 41. title()	Converts the first character of each word to upper case
print("\n\n")
print("41. title():\n")
text = "I am learning python"
x = text.title()
print(x)


# 42. translate()	Returns a translated string
print("\n\n")
print("42. translate():\n")
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))



# 43. upper()	Converts a string into upper case
print("\n\n")
print("43. upper():\n")
txt = "teju"
x = txt.upper()
print(x)



# 44. zfill()	Fills the string with a specified number of 0 values at the beginning
print("\n\n")
print("44. zfill():\n")
txt = "teju"
x = txt.zfill(10)
print(x)


