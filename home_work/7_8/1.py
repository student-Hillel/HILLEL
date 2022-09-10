cnt_user = int(input('Введите число: '))
even_num = lambda cnt_user: 'Число четное' if (cnt_user % 2 == 0) else 'Число не четное'

# print(cnt_user % 2)
print(even_num(cnt_user))