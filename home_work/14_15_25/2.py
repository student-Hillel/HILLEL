str_1 = input('Строка 1: ')
str_2 = input('Строка 2: ')
str_3 = input('Строка 3: ')
str_4 = input('Строка 4: ')

f = open('string.txt', 'w')
f.write(str_1 + '\n' + str_2)
f.close()

f = open('string.txt', 'a')
f.write('\n' + str_3 + '\n' + str_4)
f.close()
