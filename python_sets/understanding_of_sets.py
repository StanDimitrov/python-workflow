countries = {"Bulgaria","Greece","Germany","Austria"}
x = "Thayland"
y = "Japon"
z = "USA"

new_countries_set = {x,y,z}
new_countries_set.update(countries)
print(new_countries_set)

# we can create an empty set by using the set() method
new_empty_set = set()
print(new_empty_set)
new_empty_set.add(x)
print(new_empty_set)
new_list = list(new_empty_set)
print(new_list)
new_list.append("Kurdzhali")
print(type(new_list))
tul_list = set(new_list)
print(type(tul_list))

