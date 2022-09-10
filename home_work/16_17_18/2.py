'''
Прочитать сохранённый json-файл из задания №16 и записать данные на диск в csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
'''
import csv
import json

with open('task_16.json') as f:
    read_json = json.load(f)

colums = ['id', 'Name', 'Age', 'Phone']
phone = ['097-1', '097-2', '097-3', '097-4', '097-5', '097-6']

with open('task_17.csv', 'w', encoding='utf-8', newline='') as f:
    file_writer = csv.DictWriter(f, fieldnames=colums)
    file_writer.writeheader()
    x = 0
    for id, item in read_json.items():
        file_writer.writerow({'id': id, 'Name': item[0], 'Age': item[1], 'Phone': phone[x]})
        x += 1
