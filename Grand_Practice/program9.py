# Dictionary & Set

rf = {}
fr = {

    "aa" : 45,
    "bb" : 56,
    "cc" : 78,
    "dd" : 90,
    "gg" : 65,
}

# print(fr, type(fr))

rf.update({"Farman" : 60, "Kashif" : 70})
# print(rf)

# print(fr.keys(), fr.values())

a = {2, 4, 6, 7, 9, 1}
b = {5, 3, 2, 1, 0, 5}

a.union(b)
b.intersection(a)
# print(a, b)

c = {1, 7}
d = c.issubset(a)
# print(d)

e = {1, 2, 3, 5, 7}
f = e.issuperset(c)
# print(f)

s = set()
# print(type(s))

s.add(2)
s.add(4)
print(s)