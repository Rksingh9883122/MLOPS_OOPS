class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes sound")
        
        

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
    
animal = Animal("Generic Animal")
animal.speak()

        
dog = Dog('Jacky')
dog.speak()
           
class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meaws")
        
cat = Cat('Tom')
cat.speak()
           

