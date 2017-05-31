class Car:
    number_of_wheels = 4

    def __init__(self, color, number_of_doors, name):
        self.color = color
        self.number_of_doors = number_of_doors
        self.name = name

    def __str__(self):
        return ('The {} {} has {} doors and {} wheels. '.format(self.color, self.name, str(self.number_of_doors),
                str(self.number_of_wheels)))

    def honk(self):
        print('Honk!')



