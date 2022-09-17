'''
Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение,
вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.
Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
Создать своё исключение, к примеру возведение в отрицательную степень.
'''
import math

class Сalculator():
    def summ(x, y):
        result = None
        try:
            result = int(x) + int(y)
        except ValueError:
            result = x + y 
        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result

    def sub(x, y):
        result = None
        try:
            result = int(x) - int(y)
        except ValueError:
            print("Objects of the 'int' type cannot subtract objects of the 'str' type")
        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result

    def multi(x, y):
        result = None
        try:
            result = int(x) * int(y)
        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result
    
    def division(x, y):
        result = None
        try:
            result = int(x) / int(y)
        except ZeroDivisionError:
            result = 0
        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result
    
    def square(x, y):
        result = None
        try:
            result = int(x) ** int(y)

        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result

    def square_negative(x, y):
        result = None
        try:
            if int(y) < 0 or int(x) < 0:
                raise ValueError('YOU TRYING TO EXPONENT IN NEGATIVE')
            result = int(x) ** int(y)
        
        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result
    
    def square_root(x):
        result = None
        try:
            result = math.sqrt(int(x))
        except Exception as err:
            print(err)
        else:
            print('ALL IS GOED')
        finally:
            print('FINALY')
        return result

    a = input('first num: ')
    b = input('second num: ')


    print('-' * 50)
    print(summ(a, b))
    print('-' * 50)
    print(sub(a, b))
    print('-' * 50)
    print(multi(a, b))
    print('-' * 50)
    print(division(a, b))
    print('-' * 50)
    print(square(a, b))
    print('-' * 50)
    print(square_root(a))
    print('-' * 50)
    print(square_negative(a, b))

