# %% Good tutorials

# Intro
# https://realpython.com/python3-object-oriented-programming/

# How super works
# https://realpython.com/python-super/

# %%


class Animal:
    def __init__(self, species="animal_species", dangerous=True):
        self.species = species
        self.dangerous = dangerous

    def speak(self):
        pass

    def introduce(self):
        msg = f"Hi. I am a {self.species}."
        print(msg)
        if self.dangerous:
            print("Careful, I am dangerous!")


class Dog(Animal):

    sound = "Woof!"

    def __init__(self, name, color="brown"):
        super().__init__(species="dog", dangerous=False)
        self.name = name
        self.color = color

    def speak(self, times=1):
        for _ in range(times):
            print(self.sound)

    def introduce(self):
        super().introduce()
        msg = f"""
        I am a {self.color} {self.species}.
        My name is {self.name}.
        When I speak, I say {self.sound}.
        """
        print(msg)


class Cat(Animal):

    sound = "Miau!"

    def __init__(self):
        super().__init__(species="cat", dangerous=True)

    def speak(self):
        print(self.sound)
        print("Obey me human!!")


# %%

a1 = Animal()
a1.introduce()

# %%

d1 = Dog(name="Washington")
d2 = Dog(name="Don Perro", color="black")

d1.introduce()
d1.speak()

d2.introduce()
d2.speak(5)

# %%

c1 = Cat()
c1.introduce()
c1.speak()
