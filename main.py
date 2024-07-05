# converting a list to a set
my_list = [10,23,30,2,8,11]
my_set = set(my_list)
print(my_set)

#checking if an element exists in the set or not
if 30 in my_set:
    print("Element exists in set")
else:
    print("Element does not exist in set")

#adding elemnts to a set
new_set = set([])
new_set.add(6)
new_set.add(9)
new_set.add(20)

print(new_set)

#Removing elements from the set
my_set.remove(23)
# Throws error if element is not present
#my_set.remove(5)
# Does not throw error if element is not present
my_set.discard(5)

print(my_set)


#union of sets
x = {2,3,9,8,10}
y = {11,100,4,3}
union = x.union(y)
print(union)

#Intersection of sets
inter = x.intersection(y)
print(inter)

#Difference of sets
diff = x.difference(y)
print(diff)

#Symmetric differnce of sets
symm = x.symmetric_difference(y)
print(symm)