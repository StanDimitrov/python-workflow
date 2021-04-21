

names = {"Stanimir","Peter", "John","Bob","Ssarah"}
students = {}.fromkeys(names, 0.0)
print(students)

print(students["John"])
print(students.get("ABC",99.99)) # while we use .get we can add an additional key and value for it like "ABC", 99.99
