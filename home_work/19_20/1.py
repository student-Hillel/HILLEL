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

    def __init__(self, brand='Audi', color='Gray', mark='RS 6', weight='1,840 kg'):

        print(f'Brand: {brand}, Color: {color}, Mark: {mark}, Weight: {weight}')

audi_rs6 = Auto()
audi_rs6.birthday()
audi_rs6.move()
audi_rs6.stop() 