while True:
    name = input('Введите свое имя: ')
    age = input('Введите свой возраст: ')

    if name.isdigit() or not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
        continue

    elif int(age) < 10:
        print(f'Привет, шкет {name}')

    elif int(age) <= 18:
        print(f'Как жизнь, {name}?')

    elif int(age) < 100:
        print(f'Что желаете,{name}?')

    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')

    answer = input('Желаете выйти? (Y/Д): ').lower()
    if answer in ('y', 'д'): #  якшо оставляєм в дужках малі букви то пишем ловер (це ми упускаєм який регістр уведе користувач)(якшо остав великі то метод аппер)
        break
    else:
        continue