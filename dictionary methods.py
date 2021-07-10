#1. clear() - Removes all the elements from the dictionary
print("1. clear()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
dict.clear()
print(dict)




#2. copy() - Returns a copy of the dictionary
print("\n\n")
print("2. copy()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
dict2 = dict.copy()
print(dict2)


#3. fromkeys()- Returns a dictionary with the specified keys and value
print("\n\n")
print("3. fromkeys()\n")
x = { "name","place", "age"}
y = 0
dict = dict.fromkeys(x,y)
print(dict)


#4. get() - Returns the value of the specified key
print("\n\n")
print("4. get()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
x = dict.get("age")
print(x)


#5. items() - Returns a list containing a tuple for each key value pair
print("\n\n")
print("5. items()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
x = dict.items()
print(x)


#6. keys() - Returns a list containing the dictionary's keys
print("\n\n")
print("6. keys()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
x = dict.keys()
print(x)

#7. pop() - Removes the element with the specified key
print("\n\n")
print("7. pop()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
dict.pop("age")
print(dict)

#8. popitem() - Removes the last inserted key-value pair
print("\n\n")
print("8. popitem()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
dict.popitem()
print(dict)

#9. setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print("\n\n")
print("9. setdefault()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
x=dict.setdefault("name","sravs")
print(x)


#10. update() - Updates the dictionary with the specified key-value pairs
print("\n\n")
print("10. update()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
dict.update({"name":"sravs"})
print(dict)


#11. values() - Returns a list of all the values in the dictionary
print("\n\n")
print("11. values()\n")
dict = { "name":"Teju", "place":"hyd", "age":18}
x=dict.values()
print(x)
