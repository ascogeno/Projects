class Cat:

    def __init__(self, breed="Unknown", color="Unknown", eye_color="Unknown", disposition="Unknown", age=0, name="None Given"):
        self.breed = breed
        self.color = color
        self.eye_color = eye_color
        self.disposition = disposition
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name}:{self.breed}:{self.color}:{self.disposition}"

    def speak(self):
        if self.disposition == "evil":
            print(f"HISS!!! ROAR!!!!")
        elif self.disposition == "weird":
            print(f"Meep Meep Reowr!")
        elif self.disposition == "dramatic":
            print(f"To mew, or not to mew. Meow?")
        elif self.disposition == "too kind":
            print(f"Uh... meow?")
        else:
            print("Meow")
