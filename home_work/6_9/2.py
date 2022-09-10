def num(x):
    print('Ты угадал!', x)


def all_code():
    print('Число в диапазоне от 1 до 10')

    while True:
        user_cnt = int(input('Угадай число: '))

        if user_cnt == 7:
            num(7)

        elif user_cnt != 7 < 10 or user_cnt > 10:
            print('Неверно(')
            print('Попробуй еще..')
            continue

        answer = input('Хочешь еще попробовать? (y/д): ').lower()
        if answer in ('y', 'д'):
            continue

all_code()

