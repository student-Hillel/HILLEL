class String(str):

    def __add__(self, other):
        x = str(self) + str(other)
        return String(x)
    
    def __sub__(self, other):
        str_self = str(self)
        str_other = str(other)
        new_str = str_self.replace(str_other, '', 1)
        return new_str
   

print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)

print('-' * 50)

print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)

print('-' * 50)

a = String(55678345672) - 7
print(type(a))