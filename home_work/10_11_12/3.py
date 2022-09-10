values = [1, 2, '3', 'forth', 'end', 99, True, None]

new_values = list(map(lambda item: str(item) if(type(item) == int) else item,  values))
print(new_values)
