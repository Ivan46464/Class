
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sell(self) -> str:
        print(f"Animal {self.name} sold.")

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        return f"Cat - {super().__str__()}, Breed: {self.breed}"


class Dog(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def __str__(self) -> str:
        return f"Dog - {super().__str__()}, Size: {self.size}"


class PetShop:
    def __init__(self):
        self.animals = []

    def add_dog(self, name, age, size):
        dog = Dog(name, age, size)
        self.animals.append(dog)
        print(f"Added dog: {dog}")

    def add_cat(self, name, age, breed):
        cat = Cat(name, age, breed)
        self.animals.append(cat)
        print(f"Added cat: {cat}")

    def sell_dog(self, name):
        for animal in self.animals:
            if isinstance(animal, Dog) and animal.name == name:
                animal.sell()
                self.animals.remove(animal)
                return
        print(f"No dog with the name {name} found.")

    def sell_cat(self, name):
        for animal in self.animals:
            if isinstance(animal, Cat) and animal.name == name:
                animal.sell()
                self.animals.remove(animal)
                return
        print(f"No cat with the name {name} found.")

    def print_available_animals(self):
        print("Available animals:")
        for animal in self.animals:
            print(animal)


# Примерно използване на класовете и функциите

pet_shop = PetShop()

pet_shop.add_dog("Buddy", 3, "Medium")
pet_shop.add_cat("Whiskers", 5, "Persian")
pet_shop.add_dog("Max", 2, "Small")

pet_shop.print_available_animals()

pet_shop.sell_dog("Buddy")
pet_shop.sell_cat("Mittens")

pet_shop.print_available_animals()

while True:
    print("1.Add a car to the dictionary")
    print("2.Print the car with the largest srting for brand ")
    print("3.Sorted in descending order the brands")
    print("4.Save in file")
    print("5.Exit")
    choice = input("Input your choice:")
    if choice == "1":
        set1 = add1(set1)
        print(set1)
    elif choice == "2":
        sort1(set1)
    elif choice == "3":
        nai(set1)
    elif choice == "4":
        file(set1)
    elif choice == "5":
        break
    else:
        print("Wrong input passy")