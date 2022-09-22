class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# Fish inherits from Animal class
class Fish(Animal):
    def __init__(self):
        # Inherit from super class (Animal)
        super(Fish, self).__init__()

    def breathe(self):
        super(Fish, self).breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()

nemo.swim()
nemo.breathe()
