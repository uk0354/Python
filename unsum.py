a = {"apple", "banana"}
b = {"banana", "cherry"}

print("Union:", a | b)
print("Intersection:", a & b)

a.add("orange")
a.remove("banana")

print("Updated Set a:", a)
