class Mammals:
    def walk(self):
        print("Walk")

class Dog(Mammals):
    def bark(self):
        print("Bark")

class Cat(Mammals):
    def innocent(self):
        print("Innocent")

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.innocent()