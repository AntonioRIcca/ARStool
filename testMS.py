a = [1, 2, 3, 4, 5]

b = [2, 5, 6]

print(a)
print(b)
c = a
print(c)


for e in b:
    print(e)
    if e in c:
        c.remove(e)
print(c)

