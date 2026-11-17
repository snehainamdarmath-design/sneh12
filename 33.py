class animal:
    def sound(self):
        print("Animal is eating food")
class dog(animal):
    def sound(self):
        print("bow bow")
class cat(animal):
    def sound(self):
        print("meow meow")
d=dog()
c=cat()
d.sound()
c.sound()