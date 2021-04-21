
names = ["Stan","Python","John","Bob","Peter"]
scores = [97.25,96.26,82.12,99.30,100.00]
heading = "{:10} {:>20}".format("Names", "Scores")
print(heading)
print()

for name,score in zip(names,scores):
    str = "{:10} {:20}".format(name,score)
    print(str)