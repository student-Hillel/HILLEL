old_dict = {'a': 12, 'bb': False, '12': 4.5}
new_dict = {value: key for key, value in old_dict.items()}
print(new_dict)
