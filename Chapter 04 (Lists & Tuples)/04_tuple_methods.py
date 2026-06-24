a = (23, "Farman", 455, 766, 89, 90, "Python", 766, "Flast")

print(a)

no = a.count(766)
no1 = a.index(766)
print(no)
print(no1)

b = (23, 34, 76, 89, 95, 56)
concatenated_tuple = a + b
print(concatenated_tuple)

repeated = b * 3
print(repeated)

print(76 in b) # Checking if an element is present in the tuple
print(100 in b) # Checking if an element is present in the tuple)

print(len(b)) # Getting the length of the tuple)