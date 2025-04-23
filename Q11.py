l = list(input("enter in form of tuples:"))

for item in l:
    if not item:
        l.remove(item)
    else:
        continue

print(l)