# 1. add() -  Adds an element to the set
print("1. add()\n")
set = { 1, 2, 3, 4, 2, 2, 3}
set.add(5)
print(set)



# 2. clear() - Removes all the elements from the set
print("\n\n")
print("2. clear()\n")
set = { 1, 2, 3, 4, 2, 2, 3}
set.clear()
print(set)


# 3. copy() - Returns a copy of the set
print("\n\n")
print("3. copy()\n")
set = { 1, 2, 3, 4, 5}
x = set.copy()
print(x)


# 4. difference() - Returns a set containing the difference between two or more sets
print("\n\n")
print("4. difference()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.difference(set2)
print(x)



# 5. difference_update() - Removes the items in this set that are also included in another, specified set
print("\n\n")
print("5. difference_update()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
set1.difference_update(set2)
print(set1)



# 6. discard()- Remove the specified item
print("\n\n")
print("6. discard()\n")
set = { 1, 2, 3, 4, 5}
set.discard(4)
print(set)


#7. intersection() - Returns a set, that is the intersection of two or more sets
print("\n\n")
print("7. intersection()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.intersection(set2)
print(x)


# 8. intersection_update() - Removes the items in this set that are not present in other, specified set(s)
print("\n\n")
print("8. intersection_update()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
set1.intersection_update(set2)
print(set1)


#9. isdisjoint() - Returns whether two sets have a intersection or not
print("\n\n")
print("9. isdisjoint()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.isdisjoint(set2)
print(x)


# 10. issubset() - Returns whether another set contains this set or not
print("\n\n")
print("10. issubset()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.issubset(set2)
print(x)

#11. issuperset() - Returns whether this set contains another set or not
print("\n\n")
print("11. issuperset()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.issuperset(set2)
print(x)


#12. pop() - Removes an element from the set
print("\n\n")
print("12. pop()\n")
set = { 1, 2, 3, 4, 5}
set.pop()
print(set)



# 13. remove()- Removes the specified element
print("\n\n")
print("13. remove()\n")
set = { 1, 2, 3, 4, 5}
set.remove(5)
print(set)



#14. symmetric_difference() - Returns a set with the symmetric differences of two sets
print("\n\n")
print("14. symmetric_difference()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.symmetric_difference(set2)
print(x)

#15. symmetric_difference_update() - inserts the symmetric differences from this set and another
print("\n\n")
print("15. symmetric_difference_update()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
set1.symmetric_difference_update(set2)
print(set1)


#16. union() - Return a set containing the union of sets
print("\n\n")
print("16. union()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
x = set1.union(set2)
print(x)


#17. update() - Update the set with another set, or any other iterable
print("\n\n")
print("17. update()\n")
set1 = { 1, 2, 3, 4, 5}
set2 = { 4,5,6,7}
set1.update(set2)
print(set1)


