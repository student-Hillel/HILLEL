a1 = '1'
a2 = '1'
a3 = '1'
print(id(a1), id(a2), id(a3))

a1 = list(a1)
a2 = list(a2)
a3 = list(a3)

print(id(a1), id(a2), id(a3))

print(a1, a2, a3)

print( end='\n')

b1 = {1}
b2 = {1}
print(id(b1), id(b2))

b1 = bool(b1)
b2 = bool(b2)
print(id(b1), id(b2))

print(b1, b2)
