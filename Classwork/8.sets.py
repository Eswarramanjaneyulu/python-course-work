# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Creating an empty set (use set() function, not {})
empty_set = set()
# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}


#2. Set Properties
# This will raise a TypeError
#invalid_set = {[1, 2], 3}
# Lists are mutable and cannot be added to a set

#3. Operations on Sets
#a. Membership Testing
s = {1,2,3,4,5,6,7}
print(3 in s)
print(8 in s)
print(7 not in s)
print(10 not in s)

#b. Union (| or union() method)
s1={1,2,3,4}
s2={4,5,6,7}
print(s1|s2)
#c. Intersection (& or intersection() method)
print(s1&s2)
#d. Difference (- or difference() method)
print(s1-s2)
#e. Symmetric Difference (^ or symmetric_difference() method)
print(s1^s2)
#f. Subset (<= or issubset() method)
print(s1<=s2)
#g. Superset (>= or issuperset() method)
print(s1>=s2)
#h. Disjoint Sets (isdisjoint() method)
print(s1.isdisjoint(s2))
