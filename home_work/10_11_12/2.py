inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

filtered_inputdata = list(filter(lambda i: i.lower() == i.lower()[::-1], inputdata))
print(filtered_inputdata)