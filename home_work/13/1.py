def analysis_cnt(q):
    if q.isdigit():
        print(f'Целое положительное: {q}')
    if q[0] == '-':
        b = q.replace('-', '', 1)
        if b.isdigit():
            print(f'Целое отрицательное: {q}')
    t = q.replace(',', '').replace('.', '').replace('-', '')
    if t.isdigit():
        if q[0] == '-' and '-' not in q[1:]:
            f = float(q)
            print(f'Дробное отрицательное: {q}')
        elif q[0] != '-' and '-' not in q[1:]:
            f = float(q)
            if f != 0:
                print(f'Дробное положительное: {q}')


while True:
    input_user = input('''Введите число
Для выхода нажмите один из вариантов
("выход", "exit", "quit", "e", "q")
: ''').lower()
    analysis_cnt(input_user)

    if input_user in ("выход", "exit", "quit", "e", "q"):
        break
    else:
        continue 