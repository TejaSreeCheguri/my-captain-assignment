
# 1.append()-add elements to the end of the list

print("1. append()\n")
list = [ '1', '2', 'a','b']
print("before appending")
print(list)
list.append('TejaSree')
print("after appending")
print(list)

# 2. clear()-clear all elements from the list

print("\n\n")
print("2. clear()\n")
list = [ '1', '2', 'a','b']
print("before:")
print(list)
list.clear()
print("after using clear function")
print(list)


# 3. copy()- Returns a copy of the list

print("\n\n")
print("3. copy()\n")
list1 = [ '1', '2', 'a','b']
print("list1")
print(list1)
list2 = list1.copy()
print("list2")
print(list2)


# 4. count() - Returns the number of elements with the specified value

print("\n\n")
print("4. count()\n")
list1 = [ 1,2,3,4,1,2,3,4]
print("list1")
print(list1)
x = list1.count(2)
print("no of times 2 is repeated is:")
print(x)



# 5. extend() - Add the elements of a list (or any iterable), to the end of the current list

print("\n\n")
print("5. extend()\n")
list1 = [ 'a', 'b', 'c' ]
list2 = [ 'd', 'e', 'f'  ]
list1.extend(list2)
print(list1)


# 6.  index() - Returns the index of the first element with the specified value

print("\n\n")
print("6. index()\n")
list1 = [ 'a', 'b', 'c' ]
x = list1.index('b')
print(x)



# 7. insert() - Adds an element at the specified position

print("\n\n")
print("7. insert()\n")
list1 = [ 'a', 'b', 'c' ]
list1.insert(1, 'tej')
print(list1)



# 8. pop() - Removes the element at the specified position

print("\n\n")
print("8. pop()\n")
list1 = [ 'a', 'b', 'c' ]
list1.pop(1)
print(list1)




# 9. remove() - Removes the first item with the specified value

print("\n\n")
print("9. remove()\n")
list1 = [ 'a', 'b', 'c', 'a' ]
list1.remove('a')
print(list1)




# 10. reverse() - Reverses the order of the list

print("\n\n")
print("10. reverse()\n")
list1 = [ 1,2,3,4,5 ]
list1.reverse()
print(list1)



# 11. sort() - Sorts the list

print("\n\n")
print("11. sort()\n")
list1 = [ 4,6,1,5,8]
list1.sort()
print(list1)




