
a = ["aa", "bb", "cc"]
a.append("dd")
# print(a)

a.reverse()

# print(a)

a.remove("bb")
# print(a)

a.append("ee")

a.sort()
# print(a)

b = ["hh", "ii"]

b.append("kk")
b.reverse()

# print(b)

c = (23, 45, 67, 24, 90)

print(c[1:], type(c))

d = set()
d.add(3)
d.add(5)
d.add(7)
d.add(9)
d.remove(5)
print(d)