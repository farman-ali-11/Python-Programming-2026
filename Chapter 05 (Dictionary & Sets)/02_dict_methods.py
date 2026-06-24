marks = {

    "Farman" : 88,
    "Ahmed" : 50,
    "Kamran" : 67,
    20 : "Kashif",
    "Rehman" : 45
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Farman" : 99, "Nouman" : 98})
print(marks)

print(marks.get("Farman2")) # Prints None
print(marks["Farman2"]) # Returns an Error

# print(marks.popitem())
# print(marks.pop("Kamran", 67))