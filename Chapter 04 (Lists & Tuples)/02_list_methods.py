list = ["Farman", "Ahmed", 23, 4646, "Python", "Django", "Flask"]

print(list)

list.append("Java") # Adding an element at the end of the list
print(list)

list.insert(2, "C++")  # Adding an element at a specific index
print(list)

list1 = [23, 3, 5, 78, 968, 0, 6,85,86, 83]
list1.sort()
print(list1) # Sorting the list in ascending order

list1.reverse() # Reversing the list
print(list1)

a = "Farman"
a = a[::-1]  # Reversing the string
print(a)

list.pop(2) # Removing an element by index
print(list.pop(2)) # Removing an element by index and printing it

list.remove("Ahmed") # Removing an element by value
print(list)

name = "Farman Rajper"
parts = name.split()
reversed_name = parts[1] + " " + parts[0]
print(reversed_name) # Reversing the order of words in a string