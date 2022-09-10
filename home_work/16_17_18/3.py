'''
Прочитать сохранённый csv-файл из задания №17 и сохранить данные в excel-файл,
кроме возраста – столбец с этими данными не нужен.
'''
import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

my_csv_values = []

with open('task_17.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        my_csv_values.append(row)

result_wb_values = [[] for i in range(len(my_csv_values[0]))]

for index, values_list in enumerate(result_wb_values):
    for my_csv_value in my_csv_values:
        values_list.append(my_csv_value[index])

initial_line = ['Person ' + str(i + 1) for i in range(len(result_wb_values[0]) - 1)]
initial_line.insert(0, '')

ws.append(initial_line)

for result_wb_row in result_wb_values:
    ws.append(result_wb_row)

ws.delete_rows(idx=4, amount=1)
wb.save('task_18.xlsx')