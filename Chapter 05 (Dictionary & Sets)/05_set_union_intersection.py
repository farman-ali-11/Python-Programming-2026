s1 = {12, 45, 1, 45, 67, 30, 4, 9}
s2 = {7, 0, 9, 34, 32, 12, 45}

print(s1.union(s2))
print(s1.intersection(s2))

print({9, 32, 34}.issubset(s2))
print({23, 45, 8}.issubset(s1))

e = s1 - s2
print(e)