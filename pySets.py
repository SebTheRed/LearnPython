evenSet = {0, 2, 4, 6, 8, 10}
oddSet = {0, 1, 3, 5, 7, 9}


unionSet = evenSet.union(oddSet)
intersectionSet = evenSet.intersection(oddSet)
differenceSet = evenSet.difference(oddSet)
subsetSet = evenSet.issubset(oddSet)
superSet = evenSet.issuperset(evenSet)

print(unionSet)
print(intersectionSet)
print(differenceSet)
print(subsetSet)
print(superSet)


# Challenge 28
'''
Write a Python program that takes two sets and performs the following operations:

Find the union of the two sets
Find the intersection of the two sets
Find the difference of the two sets (set1 - set2)
Determine if set1 is a subset of set2
Determine if set2 is a superset of set1

mySet.add(value) #Adds a value to the set.
mySet.remove(value) #Removes a value from the set.

mySet.union(): #returns a new set containing all elements from both sets
mySet.intersection(): #returns a new set containing only elements that are in both sets
mySet.difference(): #returns a new set containing only elements that are in the first set but not in the second set
mySet.issubset(): #returns True if all elements of a set are contained in another set
mySet.issuperset(): #returns True if a set contains all elements of another set

'''
#Unlike those lists & tuples, sets cannot have multiple occurrences of the same element. 