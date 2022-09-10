from datetime import datetime

def times(func):
    def wrapper():
        time = datetime.now()
        result = func()
        print('Время выполнения: ', datetime.now() - time)
        return  result
    return wrapper

@times
def func_1():
    print('Hello Jack!')
func_1()

@times
def func_2():
    print('Hello Tom!')
func_2()