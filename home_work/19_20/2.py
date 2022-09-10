import time

class Auto():
    brand = 'Audi'
    age = 3
    color = 'Gray'
    mark = 'RS 6'
    weight = '1,840 kg'

    def move(self):
        print('Move')

    def birthday(self, age=3):
        self.age = age
        print('Age: ', age + 1)

    def stop(self):
        print('Stop')

    def __init__(self, brand, color, mark, weight):
        print(f'Brand: {brand}, Color: {color}, Mark: {mark}, Weight: {weight}')


class Truck(Auto):
    max_load = None

    def __init__(self, brand, color, mark, weight, max_load):
        super().__init__(brand, color, mark, weight)
        self.max_load = max_load
        print(f'Max load is {max_load}')

    def move(self):
       print('Attention')
       super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Car(Auto):
    max_speed = None

    def __init__(self, brand, color, mark, weight, max_speed):
        super().__init__(brand, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
       super().move()
       print(f'Max speed is {self.max_speed}')

truck_1 = Truck('Scania', 'White', 'S620', '2000', 4000)
truck_1.move()
truck_1.load()
print('-' * 50)
truck_2 = Truck('Mercedes-Benz', 'Black', 'G123', '3000', 4000)
truck_2.move()
truck_2.load()
print('-' * 50)
car_1 = Car('BMW', 'Green', 'M5', '1500', 300)
car_1.move()
car_1.birthday()
car_1.stop()
print('-' * 50)
car_2 = Car('Jaguar', 'Red', 'M2121', '1500', 400)
car_2.move()
car_2.birthday()
car_2.stop()

