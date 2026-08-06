
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
d.add(11)
d.add(13)
d.add(15)
d.add(17)
d.add(19)
d.add(21)
d.add(23)
d.add(25)
d.remove(5)
print(d)
print(type(d))

e = {
    "farman" : 60,
    "kashif" : 70,
    "ahmed" : 68,
    "ali" : 35,
    "Rehman" : 59,
    "Lakhan" : 69,
}

e.items
e.update({"Rajper" : 45})
e.update({"Lashari" : 67})
e.update({"Khan" : 90})
print(e, type(e))
