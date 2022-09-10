lst = [1, 1, 1, 15, 15]

def count_lst():
    cnt = {num_key: lst.count(num_key) for num_key in lst}
    print(cnt)

    print(cnt.get(12))
    print(cnt.get(1))    # Перевірка 3-ма способами
    print(15 in cnt)

count_lst()

