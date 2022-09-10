w1, w2 = input("Введите предложение из двух слов: ").split()

word_1 = w1
word_2 = w2

print(word_1)
print(word_2, end="\n\n")

task_1 = "? {}, {} !".format(word_1.title(), word_2.upper())[-1::-1]
print(task_1)

task_2 = "? {a}, {b} !".format(a=word_1.title(), b=word_2.upper())[-1::-1]
print(task_2)

task_3 = f"? {word_1.title()}, {word_2.upper()} !"[-1::-1]
print(task_3)

first_sentence = " {} {} ".format(word_1, word_2)

f = open("Homework_3.txt", "w")
print(first_sentence, task_1, task_2, task_3, file=f, sep=" <<<>>> ")
f.close()
