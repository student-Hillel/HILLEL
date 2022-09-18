x = int(input('x: '))
y = int(input('y: '))

def geometrical_progression(x):
    for value in range(x):
        yield y ** value
        value += 1


result = []
for item in geometrical_progression(x):
    result.append(item)
print(result)