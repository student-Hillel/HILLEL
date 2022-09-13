class Dog():
    name = 'Darman'
    paws = 4
    tail = True
    stains = None

    def __init__(self, name, paws, tail, stains):
        self.name = name
        self.paws = paws
        self.tail = tail
        self.stains = stains
    
    @staticmethod
    def say():
        print('Woof, woof')

    @classmethod
    def name_of_dog(cls):
        print(f'This is a dog, his name is {cls.name}')

    @property
    def characteristics(self):
        return print(self.name + ', ' + self.paws + ', ' + self.tail + ', ' + self.stains)


Dog.say()
Dog.name_of_dog()
a = Dog('Barsik', '4', 'long tail', 'brown')
a.characteristics

