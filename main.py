class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} кушает")

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("чик чирик")

class Mammal(Animal):
    def make_sound(self):
        print("рррррр")

class Reptile(Animal):
    def make_sound(self):
        print("шшшшшшшш")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, zoo_staff):
        self.staff.append(zoo_staff)
        print(f"Персонал {zoo_staff} добавлен в зоопарк")

class Zookeeper():
    def looks_animals(self, animal):
        print(f"Ухаживает за {animal}")

class Veterinary():
    def heal_animal(self, animal):
        print(f"Лечит {animal}")


bird1 = Bird("Воробей", 2)
mammal1 = Mammal("Лев", 5)
reptile1 = Reptile("Змея", 3)

zoo = Zoo()
keeper = Zookeeper()
vet = Veterinary()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(vet)

animal_sound(zoo.animals)
keeper.looks_animals(mammal1.name)
vet.heal_animal(bird1.name)
