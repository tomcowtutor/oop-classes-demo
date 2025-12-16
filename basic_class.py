class TalkingMixin:
    """A mixin that adds the talking ability"""

    def talk(self):
        """say something"""
        print(f"{self.name} says {self.sound}")
  
    def greet(self):
        """Greet someone"""
        print(f"Hi, I'm {self.name}")


class FlyingMixin:
    """A mixin that adds flying ability"""
    
    def fly(self):
        """Take to the air"""
        print(f"{self.name} is flying high!")
    
    def land(self):
        """Come back down"""
        print(f"{self.name} lands gracefully")


class SwimmingMixin:
    """A mixin that adds swimming ability"""
    
    def swim(self):
        """Move through water"""
        print(f"{self.name} is swimming")
    
    def dive(self):
        """Go underwater"""
        print(f"{self.name} dives deep")


class ColourMixin:
    """A mixin that adds colour"""
    def __init__(self, colour="unknown"):
        self.colour = colour
    
    def show_info(self):
        """displays additional info"""
        print(f"   Colour: {self.colour}   ")


class Animal:
    """Base class for all animals"""
    def __init__(self, name, age, sound):
        """Creates an instance of animal"""
        self.name = name
        self.age = age
        self.sound = sound

    def makes_sound(self):
        """The animal makes its characteristic sound"""
        print(f"{self.name} says: {self.sound}")

    def eat(self):
        """The animal eats"""
        print(f"{self.name} is eating")

    def sleep(self):
        """The animal sleeps"""
        print(f"{self.name} is sleeping")

    def birthday(self):
        """The animal has a birthday"""
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

    def show_info(self):
        """displays animal info"""
        print(f"--- {self.__class__.__name__}: {self.name} ---")
        print(f"  Age: {self.age}   ")
        print(f"  Sound: {self.sound}   ")


class Parrot(TalkingMixin, FlyingMixin, Animal):
    """A class representing a parrot -- inherits from Animal"""
    def __init__(self, name, age, sound="Squawk!"):
        super().__init__(name, age, sound)


class Duck(FlyingMixin, SwimmingMixin, Animal):
    """A class representing a duck -- inherits from Animal"""
    def __init__(self, name, age, sound="Quack!"):
        super().__init__(name, age, sound)


class Fish(SwimmingMixin, ColourMixin, Animal):
    """A class representing a fish -- inherits from Animal"""
    def __init__(self, name, age, sound="blub blub"):
        super().__init__(name, age, sound)

    def blow_bubbles(self):
        """Blow air bubbles"""
        print(f"{self.name} blows bubbles!")


class Dog(TalkingMixin, Animal,  ColourMixin):
    """A class representing a dog -- inherits from Animal"""
    def __init__(self, name, age, sound="Woof Woof!", breed="unknown"):
        super().__init__(name, age, sound)
        self.breed = breed
        self.tricks = []

    def learn_trick(self, trick_name):
        """Learn a new trick"""
        if trick_name in self.tricks:
            print(f"{self.name} already knows how to {trick_name}")
        else:
            self.tricks.append(trick_name)
            print(f"{self.name} learned a new trick: {trick_name}")

    def perform_trick(self, trick_name):
        """Perform a trick"""
        if trick_name in self.tricks:
            print(f"{self.name} performs the trick: {trick_name}! Awesome")
        else:
            print(f"{self.name} doesn't know the trick: {trick_name}")

    def show_info(self):
        """displays extra dog info"""
        super().show_info()
        print(f"  Breed: {self.breed}   ")
        print(f"  Tricks: {self.tricks}   ")


Wren = Dog("Wren", 5, "woof", "Karst Shepherd")
Nettle = Dog("Nettle", 1, "woof", "Golden Retriever")


Wren.learn_trick("Sit")
Wren.learn_trick("Sit")
Wren.learn_trick("Roll Over")
Wren.learn_trick("Stay")
Wren.perform_trick("High Five")

Wren.show_info()


# Polly = Parrot("Polly", 34)

# Polly.greet()